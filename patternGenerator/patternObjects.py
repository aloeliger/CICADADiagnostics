from utilities import *
from eventObjects import *
from pathlib import Path

import numpy as np

#base class for a set of pattern functions + data
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


#Set of patterns for regions. Basically 1 files worth
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

# Set of emulator patterns. Basically one file's worth
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

# A complete collection of region patterns. Potentially many files worth
class RegionPatternCollection():
    def __init__(self, outputLocation = 'testVectors/inputs'):
        self.currentRegionPatternSet = None
        self.regionPatternSets = []
        self.outputLocation = Path(outputLocation)
        self.outputLocation.mkdir(exist_ok=True, parents=True)

    def insertEvent(self, theEvent: Event):
        if self.currentRegionPatternSet == None:
            self.currentRegionPatternSet = RegionPatternSet()
            self.currentRegionPatternSet.insertEvent(theEvent)
            return
        else:
            if len(self.currentRegionPatternSet.events) == self.currentRegionPatternSet.requiredEvents:
                self.regionPatternSets.append(self.currentRegionPatternSet)
                self.currentRegionPatternSet = RegionPatternSet()
            self.currentRegionPatternSet.insertEvent(theEvent)
            return

    def dumpOutPatternCollection(self):
        if self.currentRegionPatternSet is not None:
            self.regionPatternSets.append(self.currentRegionPatternSet)
            self.currentRegionPatternSet = None
        for index, patternSet in enumerate(self.regionPatternSets):
            patternSet.fillEmptyEvents()
            with open(self.outputLocation / f'testPatterns_{index}.txt', 'w+') as theFile:
                regionPatternString = patternSet.getCompletePatternString()
                theFile.write(regionPatternString)

# A complete collection of model scores/results. Potentially many files worth.
class ModelScorePatternCollection():
    def __init__(self, outputLocation = 'testVectors/outputs'):
        self.currentModelScorePatternSet = None
        self.modelScorePatternSets = []
        self.outputLocation = Path(outputLocation)
        self.outputLocation.mkdir(exist_ok=True, parents=True)

    def insertEvent(self, theEvent: Event):
        if self.currentModelScorePatternSet == None:
            self.currentModelScorePatternSet = ModelScorePatternSet()
            self.currentModelScorePatternSet.insertEvent(theEvent)
            return
        else:
            if len(self.currentModelScorePatternSet.events) == self.currentModelScorePatternSet.requiredEvents:
                self.modelScorePatternSets.append(self.currentModelScorePatternSet)
                self.currentModelScorePatternSet = ModelScorePatternSet()
            self.currentModelScorePatternSet.insertEvent(theEvent)
            return

    def dumpOutPatternCollection(self):
        if self.currentModelScorePatternSet is not None:
            self.modelScorePatternSets.append(self.currentModelScorePatternSet)
            self.currentModelScorePatternSet = None
        for index, modelScorePatternSet in enumerate(self.modelScorePatternSets):
            modelScorePatternSet.fillEmptyEvents()
            with open(self.outputLocation / f'testPatterns_{index}_output.txt','w+') as theFile:
                modelScorePatternString = modelScorePatternSet.getCompletePatternString()
                theFile.write(modelScorePatternString)
