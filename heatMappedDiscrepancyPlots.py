import ROOT
import argparse
from rich.console import Console
from rich.progress import track
from pathlib import Path
import numpy as np

console = Console()

def drawHeatMap(histogram, outputPath, histName):
    theCanvas = ROOT.TCanvas(histName)
    histogram.Draw("COLZ")
    histogram.GetXaxis().SetTitle('iEta')
    histogram.GetYaxis().SetTitle('iPhi')
    histogram.SetTitle('')

    theCanvas.SaveAs(
        str(
            outputPath/f"{histName}.png"
        )
    )

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(args.fileIn)

    runTree = theFile.l1EventTree.L1EventTree
    emuTree = theFile.l1CaloSummaryEmuTree.L1CaloSummaryTree
    unpackTree = theFile.l1CaloSummaryTree.L1CaloSummaryTree

    nEntries = emuTree.GetEntries()

    discrepancies = []

    outputPath = Path(args.outputPath)
    outputPath.mkdir(exist_ok=True)

    regionOccupancy = ROOT.TH2D(
        'regionOccupancy',
        'regionOccupancy',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0
    )
    EtWeightedRegionOccupancy = ROOT.TH2D(
        'EtWeightedRegionOccupancy',
        'EtWeightedRegionOccupancy',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0
    )

    DiscrepancyOnly_RegionOccupancy = ROOT.TH2D(
        'DiscrepancyOnly_RegionOccupancy',
        'DiscrepancyOnly_RegionOccupancy',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0
    )
    DiscrepancyOnly_EtWeightedRegionOccupancy = ROOT.TH2D(
        'DiscrepancyOnly_EtWeightedRegionOccupancy',
        'DiscrepancyOnly_EtWeightedRegionOccupancy',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0
    )
    DiscrepancyOnly_EtDiscrepancyWeightedRegionOccupancy = ROOT.TH2D(
        'DiscrepancyOnly_EtDiscrepancyWeightedRegionOccupancy',
        'DiscrepancyOnly_EtDiscrepancyWeightedRegionOccupancy',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0
    )
    
    for index in track(range(nEntries), description='Events'):
        emuTree.GetEntry(index)
        unpackTree.GetEntry(index)
        runTree.GetEntry(index)

        run = int(runTree.GetLeaf("run").GetValue())
        event = int(runTree.GetLeaf("event").GetValue())

        emuScore = emuTree.GetLeaf("CICADAScore").GetValue()
        firmwareScore = unpackTree.GetLeaf("CICADAScore").GetValue()
        discrepancy = abs(emuScore-firmwareScore)

        discrepancies.append((run, event, discrepancy))

        regions = np.zeros((18,14))
        
        for i in range(252):
            iPhi = i // 14
            iEta = i % 14
            regions[iPhi][iEta] = emuTree.GetLeaf('modelInput').GetValue(i)

            if regions[iPhi][iEta] != 0.0:
                regionOccupancy.Fill(iEta, iPhi)
            EtWeightedRegionOccupancy.Fill(iEta, iPhi, regions[iPhi][iEta])

            if discrepancy != 0.0:
                if regions[iPhi][iEta] != 0.0:
                    DiscrepancyOnly_RegionOccupancy.Fill(iEta, iPhi)
                DiscrepancyOnly_EtWeightedRegionOccupancy.Fill(
                    iEta,
                    iPhi,
                    regions[iPhi][iEta]
                )
                DiscrepancyOnly_EtDiscrepancyWeightedRegionOccupancy.Fill(
                    iEta,
                    iPhi,
                    regions[iPhi][iEta]*discrepancy
                )
            

    discrepancies.sort(
        key= lambda x: x[2]
    )
    #console.print(
    #    discrepancies[-256:]
    #)
    drawHeatMap(
        regionOccupancy,
        outputPath,
        histName='regionOccupancy'
    )
    drawHeatMap(
        EtWeightedRegionOccupancy,
        outputPath,
        histName='EtWeightedRegionOccupancy'
    )
    drawHeatMap(
        DiscrepancyOnly_RegionOccupancy,
        outputPath,
        histName='DiscrepancyOnly_RegionOccupancy'
    )
    drawHeatMap(
        DiscrepancyOnly_EtWeightedRegionOccupancy,
        outputPath,
        histName='DiscrepancyOnly_EtWeightedRegionOccupancy'
    )
    drawHeatMap(
        DiscrepancyOnly_EtDiscrepancyWeightedRegionOccupancy,
        outputPath,
        histName='DiscrepancyOnly_EtDiscrepancyWeightedRegionOccupancy'
    )
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check for highest discrepancies, and highest discrepant regions')

    parser.add_argument(
        '--fileIn',
        required=True,
        nargs='?',
        help='File to make plots for',
    )
    parser.add_argument(
        '--outputPath',
        default='./HeatMappedDiscrepancies',
        nargs='?',
        help='Spot to put the plots'
    )

    args = parser.parse_args()

    main(args)
