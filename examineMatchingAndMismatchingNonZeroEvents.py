import argparse
from rich.console import Console
from rich.progress import track
from pathlib import Path
import termplotlib as tpl
import numpy as np
import statistics
import ROOT

console = Console()

class fileResults():
    def __init__(self):
        self.emulatorScores = []
        self.unpackedScores = []

        self.emulatedRegions = []
        self.unpackedRegions = []
        
        self.regionDiscrepancies = []
        self.scoreDiscrepancies = []
        self.nEvents = 0

    def addEventData(self, theEventData):
        self.emulatorScores.append(theEventData.emuScore)
        self.unpackedScores.append(theEventData.unpackScore)

        self.emulatedRegions += theEventData.emuRegions
        self.unpackedRegions += theEventData.unpackedRegions
        
        self.regionDiscrepancies += theEventData.regionDiscrepancies
        self.scoreDiscrepancies.append(theEventData.scoreDiscrepancy)
        self.nEvents += 1

class eventData():
    def __init__(self, emuTree, unpackTree, eventTree):
        self.emuScore = emuTree.GetLeaf("CICADAScore").GetValue()
        self.unpackScore = unpackTree.GetLeaf("CICADAScore").GetValue()
        self.scoreDiscrepancy = self.emuScore - self.unpackScore

        self.run = int(eventTree.GetLeaf('run').GetValue())
        self.event = int(eventTree.GetLeaf('event').GetValue())
        self.lumi = int(eventTree.GetLeaf('lumi').GetValue())
        
        self.emuRegions = []
        self.unpackedRegions = []
        self.regionDiscrepancies = []
        for i in range(252):
            emuRegion = emuTree.GetLeaf("modelInput").GetValue(i)
            unpackedRegion = unpackTree.GetLeaf("modelInput").GetValue(i)
            self.emuRegions.append(
                emuRegion
            )
            self.unpackedRegions.append(
                unpackedRegion
            )

            regionDiscrepancy = emuRegion - unpackedRegion
            self.regionDiscrepancies.append(
                regionDiscrepancy
            )
            
def makeTermHistogram(theList):
    counts, bin_edges = np.histogram(theList, bins=20)
    histo = tpl.figure()
    histo.hist(counts, bin_edges, orientation='horizontal')
    histo.show()

def dumpFileResults(fileResults):
    console.print('Emulator Scores')
    makeTermHistogram(fileResults.emulatorScores)
    console.print()
    console.print('Unpack Scores')
    makeTermHistogram(fileResults.unpackedScores)
    console.print()
    console.print('Score Discrepancies')
    makeTermHistogram(fileResults.scoreDiscrepancies)
    console.print()
    console.print('Region discrepancies')
    makeTermHistogram(fileResults.regionDiscrepancies)
    console.print()

    
def main(args):
    theFile = ROOT.TFile(args.ntupleFile)

    eventTree = theFile.l1EventTree.L1EventTree
    emuTree = theFile.l1CaloSummaryEmuTree.L1CaloSummaryTree
    unpackTree = theFile.l1CaloSummaryTree.L1CaloSummaryTree

    nEntries = unpackTree.GetEntries()

    matchingResults = fileResults()
    nonMatchingResults = fileResults()

    nonZeroEvents = 0
    runs = []
    
    console.print(f'Processing: {nEntries:>6d} Events')
    for index in track(range(nEntries), description='finding discrepencies'):
        eventTree.GetEntry(index)
        emuTree.GetEntry(index)
        unpackTree.GetEntry(index)

        theEventData = eventData(emuTree, unpackTree, eventTree)

        if theEventData.emuScore == 0.0:
            continue

        nonZeroEvents += 1
        if theEventData.run not in runs:
            runs.append(theEventData.run)
        if theEventData.scoreDiscrepancy == 0.0:
            matchingResults.addEventData(theEventData)
        else:
            nonMatchingResults.addEventData(theEventData)

    console.print('Considered runs:')
    console.print(runs)
    console.rule(f'Matching Events: {matchingResults.nEvents}')
    dumpFileResults(matchingResults)

    console.rule(f'Non-Matching Events: {nonMatchingResults.nEvents}')
    dumpFileResults(nonMatchingResults)
    console.rule()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Examine match and mismatching event propertices for non-trivial CICADA events')
    parser.add_argument(
        '--ntupleFile',
        '-n',
        type=str,
        required=True,
        nargs='?',
        help='L1Ntuple file to examine',
    )

    args = parser.parse_args()
    main(args)
