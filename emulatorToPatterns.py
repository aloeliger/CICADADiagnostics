#from huggingface_hub import from_pretrained_keras
import ROOT
import argparse
import numpy as np
import itertools
from rich.console import Console
from rich.progress import track

console = Console()

#Basic holder for our region information
class Region():
    def __init__(self, iPhi, iEta, Et):
        self.iPhi = int(iPhi)
        self.iEta = int(iEta)
        self.Et = int(Et)

#utility when we format a link
def leftPadString(string, desiredLen, char='0'):
    if len(string) >= desiredLen:
        return string
    else:
        return (desiredLen - len(string))*char+string

# Class representing a link's pattern output + information (7 regions)
class Link():
    def __init__(self, iPhi, isPosEta):
        self.iPhi = iPhi
        self.isPosEta = isPosEta
        self.regions = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ]
        
    def insertRegion(self, theRegion: Region):
        # we will store regions such that low index is low bit number, is further right on the word
        if theRegion.iPhi != self.iPhi:
            print("Tried to insert a region into a link of non-matching iPhi")
            print(f"Region iPhi: {theRegion.iPhi}, link iPhi: {self.iPhi}")
            print("Skipping, this will likely cause issues")
            return
        
        if self.isPosEta: #positive eta, regions go in ascending order, 0 bit on the right
            #iEta goes from 7 to 13,
            index = theRegion.iEta - 7
            self.regions[index] = theRegion
        else: #negative eta, regions go in descending order, 0 bit on the right

            index = 6-theRegion.iEta
            self.regions[index] = theRegion
    
    def getWord(self, numWord):
        #each word is 8 hex digis = 32 bits

        #For word 0:
        #We give two 8 bits (two digits) worth of CRC/comma (0's for our purpose)
        #then 16 bits (4 digits) worth of index 0 (low side)
        #then 8 bits (2 digits) worth of index 1 
        if numWord == 0:
            indexOneString = hex( 0xFF & self.regions[1].Et)[2:]
            indexOneString = leftPadString(indexOneString, 2)

            indexZeroString = hex(self.regions[0].Et)[2:]
            indexZeroString = leftPadString(indexZeroString, 4)

            emptyChar = '00'
            return f'0x{indexOneString}{indexZeroString}{emptyChar}'
        
        # For word 1:
        # We give the top 8 bits worth of index 1 (2 digits)
        # We give the entirety of index 2 (4 digits)
        # We give the bottom 8 bits of index 3 (2 digits)
        elif numWord == 1:
            indexOneString = hex(0xFF00 & self.regions[1].Et)[2:]
            indexOneString = leftPadString(indexOneString, 2)

            indexTwoString = hex(self.regions[2].Et)[2:]
            indexTwoString = leftPadString(indexTwoString, 4)

            indexThreeString = hex(0xFF & self.regions[3].Et)[2:]
            indexThreeString = leftPadString(indexThreeString, 2)
            return f'0x{indexThreeString}{indexTwoString}{indexOneString}'

        #For word 2:
        # We give the top 8 bits of index 3 (2 digits)
        # we give the entirety of index 4 (4 digits)
        # and we give the bottom 8 bits of index 5 (4 digits)
        elif numWord == 2:
            indexThreeString = hex(0xFF00 & self.regions[3].Et)[2:]
            indexThreeString = leftPadString(indexThreeString, 2)

            indexFourString = hex(self.regions[4].Et)[2:]
            indexFourString = leftPadString(indexFourString, 4)

            indexFiveString = hex(0xFF & self.regions[5].Et)[2:]
            indexFiveString = leftPadString(indexFiveString, 2)
            return f'0x{indexFiveString}{indexFourString}{indexThreeString}'
        # for the final word, we give the top 8 bits of index 5 (2 digits)
        # we give all of index 6 (final index, 4 digits)
        # then 8 bits/ 2 digits worth of empty CRC/Comma
        elif numWord == 3:
            emptyChar = '00'

            indexFiveString = hex(0xFF00 & self.regions[5].Et)[2:]
            indexFiveString = leftPadString(indexFiveString, 2)

            indexSixString = hex(self.regions[6].Et)[2:]
            indexSixString = leftPadString(indexSixString, 4)

            return f'0x{emptyChar}{indexSixString}{indexFiveString}'
        else:
            return None

class RegionPatternSet():
    pass
        
#class representing an event's worth of information (36 links)
class Event():
    def __init__(self):
        self.links = []
        for i in range(36):
            self.links.append(
                Link(
                    iPhi = i // 2,
                    isPosEta = (i % 2 == 1)
                )
            )
        self.modelScore = 0.0

    def insertRegion(self, theRegion: Region):
        #determine the correct link to put this thing on
        linkNo = theRegion.iPhi * 2
        #look at the iEta, if 7-13, that's positive etas
        # and we add one to the link number
        if theRegion.iEta >= 7 and theRegion.iEta <= 13:
            linkNo += 1
        self.links[linkNo].insertRegion(theRegion)

    def insertRegionGrid(self, regionGrid):
        for iPhi in range(18):
            for iEta in range(14):
                theRegion = Region(iPhi, iEta, regionGrid[iPhi][iEta])
                self.insertRegion(theRegion)

    def getLine(self, lineNo):
        lineText = ''
        for linkNo in range(36):
            #Note to self, one space either side, plus 10 characters worth of string, 12 characters
            lineText += f' {self.links[linkNo].getWord(lineNo)} '
        return lineText

    def hexModelScore(self):
        return leftPadString(hex(int(self.modelScore * 2.0**8))[2:], 4)

    def getModelScoreLine(self, lineNo):
        # 6 possible lines to read
        if lineNo >= 0 and lineNo <= 3:
            return ' 0x'+self.hexModelScore()[lineNo]+'0000000 '
        else:
            return ' 0x00000000 '

class PatternSet():
    def __init__(self):
        self.events = []
        self.requiredEvents = 256

    def insertEvent(self, theEvent):
        if len(self.events) >= self.requiredEvents:
            return
        else:
            self.events.append(theEvent)

    def fillEmptyEvents(self):
        if len(self.events) < self.requiredEvents:
            for i in range(self.requiredEvents - len(self.events)):
                newEvent = Event()
                emptyRegions = np.zeros((18, 14))
                newEvent.insertRegionGrid(emptyRegions)
                self.events.append(newEvent)

            
class RegionPatternSet(PatternSet):

    # fill out a complete set with empty events, if it isn't complete
                
    def getCompletePatternString(self):
        result = ''

        topLine = '='*438+'\n'
        result += topLine
        
        linkLine = 'WordCnt'
        for i in range(36):
            linkQuote = f'LINK_{i:02d}'
            linkString = f'{linkQuote:^12}'
            linkLine+= linkString
        linkLine += '\n'
        result += linkLine
        
        beginDataLine = '#BeginData\n'
        result+= beginDataLine
        
        for eventIndex, theEvent in enumerate(self.events):
            for lineNo in range(4):
                lineString = hex(eventIndex*4+lineNo)[2:]
                lineString = '0x'+leftPadString(lineString, 4)+' '
                lineString += theEvent.getLine(lineNo)
                lineString += '\n'
                result += lineString
        return result

class ModelScorePatternSet(PatternSet):
    def getCompletePatternString(self):
        result = ''

        topLine = '='*30+'\n'
        result += topLine
        
        linkLine = 'WordCnt'
        for i in range(2):
            linkQuote = f'LINK_{i:02d}'
            linkString = f'{linkQuote:^12}'
            linkLine += linkString
        linkLine += '\n'
        result += linkLine

        beginDataLine = '#BeginData\n'
        result+=beginDataLine

        for eventIndex, theEvent in enumerate(self.events):
            for lineNo in range(6):
                lineString = hex(eventIndex*4+lineNo)[2:]
                lineString = '0x'+leftPadString(lineString, 4)+' '
                lineString += theEvent.getModelScoreLine(lineNo)
                lineString += '\n'
                result += lineString
        return result
    
def main(args):
    #model = from_pretrained_keras("cicada-project/cicada-v2.1")

    theFile = ROOT.TFile(args.file)
    emuTree = theFile.l1CaloSummaryEmuTree.L1CaloSummaryTree
    unpackTree = theFile.l1CaloSummaryTree.L1CaloSummaryTree

    nEntries = emuTree.GetEntries()

    regionPatterns = RegionPatternSet()
    scorePatterns = ModelScorePatternSet()
    
    for entry in track(range(nEntries), description='events'):
        emuTree.GetEntry(entry)
        unpackTree.GetEntry(entry)

        emuScore = emuTree.GetLeaf("CICADAScore").GetValue()
        firmwareScore = unpackTree.GetLeaf("CICADAScore").GetValue()
        discrepancy = emuScore - firmwareScore

        if discrepancy == 0.0:
            continue
        
        regions = np.zeros((18, 14))
        for i in range(252):
            iPhi = i // 14
            iEta = i % 14
            regions[iPhi][iEta] = emuTree.GetLeaf('modelInput').GetValue(i)
        theEvent = Event()
        theEvent.insertRegionGrid(regions)
        theEvent.modelScore = emuScore

        regionPatterns.insertEvent(theEvent)
        scorePatterns.insertEvent(theEvent)
        
    regionPatterns.fillEmptyEvents()
    scorePatterns.fillEmptyEvents()
    patternString = regionPatterns.getCompletePatternString()
    modelString = scorePatterns.getCompletePatternString()

    #console.print(patternString)
    with open('testPatterns.log', 'w+') as resultFile:
        resultFile.write(patternString)

    with open('testPatternOutputs.log', 'w+') as outputResultFile:
        outputResultFile.write(modelString)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the emulator on L1 Ntuples, looking for discrepnacies, and making patterns from those events')
    parser.add_argument(
        '--file',
        required=True,
        nargs='?'
    )

    args = parser.parse_args()

    main(args)
