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

console = Console()

def main(args):
    theFile = ROOT.TFile(args.ntupleFile)
    
    emuTree = theFile.l1CaloSummaryEmuTree.L1CaloSummaryTree
    unpackTree = theFile.l1CaloSummaryTree.L1CaloSummaryTree

    #emuTree.Print()
    #unpackTree.Print()
    nEntries = unpackTree.GetEntries()
    discrepancies = []
    unpackedRegions = []
    emulatedRegions = []
    regionDiscrepancies=[]
    console.print(f'Processing: {nEntries:>6d} Events')
    #for index in track(range(nEntries), description='Finding discrepancies'):
    for index in range(nEntries):
        emuTree.GetEntry(index)
        unpackTree.GetEntry(index)

        #discrepancy = emuTree.CICADAScore - unpackTree.CICADAScore
        emuScore = emuTree.GetLeaf("CICADAScore").GetValue()
        unpackScore = unpackTree.GetLeaf("CICADAScore").GetValue()
        discrepancy = emuScore - unpackScore
        discrepancies.append(discrepancy)

        for i in range(252):
            emuRegion = emuTree.GetLeaf("modelInput").GetValue(i)
            unpackedRegion = emuTree.GetLeaf("modelInput").GetValue(i)
            unpackedRegions.append(unpackedRegion)
            emulatedRegions.append(emuRegion)
            regionDiscrepancies.append(emuRegion-unpackedRegion)
        
    console.print("Emulator - Calo Crate CICADA Score")
    counts, bin_edges = np.histogram(discrepancies, bins=20)
    histo = tpl.figure()
    #histo.hist(counts, bin_edges, orientation='horizontal', force_ascii=True)
    histo.hist(counts, bin_edges, orientation='horizontal')
    histo.show()
    console.print()

    console.print("Unpacked Region ETs")
    counts, bin_edges = np.histogram(unpackedRegions, bins=20)
    histo = tpl.figure()
    #histo.hist(counts, bin_edges, orientation='horizontal', force_ascii=True)
    histo.hist(counts, bin_edges, orientation='horizontal')
    histo.show()
    console.print()

    console.print("Emulated Region ETs")
    counts, bin_edges = np.histogram(emulatedRegions, bins=20)
    histo = tpl.figure()
    #histo.hist(counts, bin_edges, orientation='horizontal', force_ascii=True)
    histo.hist(counts, bin_edges, orientation='horizontal')
    histo.show()
    console.print()

    console.print("Region Discrepancies")
    counts, bin_edges = np.histogram(regionDiscrepancies, bins=20)
    histo = tpl.figure()
    #histo.hist(counts, bin_edges, orientation='horizontal', force_ascii=True)
    histo.hist(counts, bin_edges, orientation='horizontal')
    histo.show()
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
