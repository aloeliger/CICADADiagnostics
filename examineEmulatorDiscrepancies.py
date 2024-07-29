# !/usr/bin/env python3
# Script designed to check the L1 Ntuple produced from the first step
# And look at Calo crate versus emulator discrepancy

import argparse
from rich.console import Console
from rich.progress import track
from pathlib import Path
import ROOT
import termplotlib as tpl
import numpy as np
import statistics

console = Console()

def makeTermHistogram(theList):
    counts, bin_edges = np.histogram(theList, bins=20)
    histo = tpl.figure()
    histo.hist(counts, bin_edges, orientation='horizontal')
    histo.show()
    
def main(args):
    theFile = ROOT.TFile(args.ntupleFile)
    
    emuTree = theFile.l1CaloSummaryEmuTree.L1CaloSummaryTree
    unpackTree = theFile.l1CaloSummaryTree.L1CaloSummaryTree

    #emuTree.Print()
    #unpackTree.Print()
    nEntries = unpackTree.GetEntries()
    emuScores = []
    crateScores = []
    emuOnlyScores = []
    crateOnlyScores = []
    discrepancies = []
    noDiscrepancyScores = []
    unpackedRegions = []
    emulatedRegions = []
    regionDiscrepancies=[]
    nNoDiscrepancy = 0
    console.print(f'Processing: {nEntries:>6d} Events')
    #for index in track(range(nEntries), description='Finding discrepancies'):
    for index in range(nEntries):
        emuTree.GetEntry(index)
        unpackTree.GetEntry(index)

        #discrepancy = emuTree.CICADAScore - unpackTree.CICADAScore
        emuScore = emuTree.GetLeaf("CICADAScore").GetValue()
        unpackScore = unpackTree.GetLeaf("CICADAScore").GetValue()
        emuScores.append(emuScore)
        crateScores.append(unpackScore)
        discrepancy = emuScore - unpackScore
        discrepancies.append(discrepancy)
        if discrepancy == 0.0:
            nNoDiscrepancy += 1
            noDiscrepancyScores.append(emuScore)
        else:
            emuOnlyScores.append(emuScore)
            crateOnlyScores.append(unpackScore)

        for i in range(252):
            emuRegion = emuTree.GetLeaf("modelInput").GetValue(i)
            unpackedRegion = unpackTree.GetLeaf("modelInput").GetValue(i)
            unpackedRegions.append(unpackedRegion)
            emulatedRegions.append(emuRegion)
            regionDiscrepancies.append(emuRegion-unpackedRegion)

    console.print("Emulator scores")
    makeTermHistogram(emuScores)
    console.print()

    console.print("Unpacked Calo Crate Scores")
    makeTermHistogram(crateScores)
    console.print()
    
    console.print("Emulator - Calo Crate CICADA Score")
    console.print(f"No Discrepancy: {nNoDiscrepancy/nEntries:2.2%}")
    discrepancyMean = statistics.mean(discrepancies)
    discrepancyStdDev = statistics.pstdev(discrepancies)
    console.print(f'Mean Discrepancy: {discrepancyMean:2.2f}')
    console.print(f'Discrepancy Std Deviation: {discrepancyStdDev:2.2f}')
    makeTermHistogram(discrepancies)
    console.print()

    console.print("Agreed upon scores")
    makeTermHistogram(noDiscrepancyScores)
    console.print()

    console.print("Crate Only Scores")
    makeTermHistogram(crateOnlyScores)
    console.print()

    console.print("Emulator Only Scores")
    makeTermHistogram(emuOnlyScores)
    console.print()
    
    console.print("Unpacked Region ETs")
    makeTermHistogram(unpackedRegions)
    console.print()

    console.print("Emulated Region ETs")
    makeTermHistogram(emulatedRegions)
    console.print()

    console.print("Region Discrepancies")
    makeTermHistogram(regionDiscrepancies)
    console.print()


if __name__ == '__main__':
    parser =argparse.ArgumentParser(description='Dump histograms for emulator discrepancies')

    parser.add_argument(
        '--ntupleFile',
        '-n',
        type=str,
        required=True,
        nargs='?',
        help='L1 Ntuple file to examine',
    )

    args = parser.parse_args()
    main(args)
