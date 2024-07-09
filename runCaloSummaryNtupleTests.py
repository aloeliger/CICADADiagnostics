import ROOT
import argparse
from rich.console import Console
from rich.progress import track
from pathlib import Path
from array import array
import uproot

console = Console()

def drawScorePlots(unpackedScores, emulatedScores, outputPath):
    histName = 'scorePlots'
    theCanvas = ROOT.TCanvas(histName)
    unpackedScores.SetLineWidth(2)
    emulatedScores.SetLineWidth(2)

    unpackedScores.SetLineColor(ROOT.kRed)
    emulatedScores.SetLineColor(ROOT.kBlue)

    unpackedScores.Draw('HIST')
    emulatedScores.Draw('HIST SAME')

    unpackedScores.SetTitle("")
    unpackedScores.GetXaxis().SetTitle("CICADA Score")
    unpackedScores.GetYaxis().SetTitle("Events")

    unpackedScores.GetYaxis().SetRangeUser(
        0.0,
        max(unpackedScores.GetMaximum(), emulatedScores.GetMaximum())*1.1
    )

    theLegend = ROOT.TLegend(0.6, 0.6, 0.9, 0.9)
    theLegend.AddEntry(unpackedScores, "Unpacked FED 1356 CICADA Scores", 'l')
    theLegend.AddEntry(emulatedScores, "Emulated CICADA Scores", "l")
    theLegend.SetFillStyle(0)
    theLegend.SetLineWidth(0)

    theLegend.Draw()

    theCanvas.SaveAs(
        str(outputPath/f"{histName}.png")
    )

def drawScoreDifferencePlot(scoreDifference, histName, axisLabel, outputPath):
    theCanvas = ROOT.TCanvas(histName)
    scoreDifference.SetLineWidth(2)
    
    scoreDifference.SetLineColor(ROOT.kRed)

    scoreDifference.Draw("HIST")
    scoreDifference.GetXaxis().SetTitle(axisLabel)
    scoreDifference.GetYaxis().SetTitle("Events")
    scoreDifference.SetTitle("")

    theLegend = ROOT.TLegend(0.6, 0.6, 0.9, 0.9)
    theLegend.AddEntry(scoreDifference, "Score Difference", 'l')
    theLegend.SetFillStyle(0)
    theLegend.SetLineWidth(0)

    theLegend.Draw()

    theCanvas.SaveAs(
        str(outputPath/f"{histName}.png")
    )

def drawEventInput(exampleInput, histName, outputPath):
    theCanvas = ROOT.TCanvas(histName)
    exampleInput.Draw("COLZ")
    exampleInput.GetZaxis().SetRangeUser(0, 25.0)
    
    exampleInput.GetXaxis().SetTitle("iEta")
    exampleInput.GetYaxis().SetTitle("iPhi")
    exampleInput.SetTitle("")

    theCanvas.SaveAs(
        str(outputPath/f"{histName}.png")
    )

def drawEventETs(unpackedETs, emulatedETs, outputPath, histName='eventETs'):
    theCanvas = ROOT.TCanvas(histName)
    unpackedETs.SetLineWidth(2)
    emulatedETs.SetLineWidth(2)

    unpackedETs.SetLineColor(ROOT.kRed)
    emulatedETs.SetLineColor(ROOT.kBlue)

    unpackedETs.Draw("HIST")
    emulatedETs.Draw("HIST SAME")

    unpackedETs.SetTitle("")
    unpackedETs.GetXaxis().SetTitle("ET")
    unpackedETs.GetYaxis().SetTitle("Counts")

    unpackedETs.GetYaxis().SetRangeUser(
        0.0,
        max(unpackedETs.GetMaximum(), emulatedETs.GetMaximum())*1.1
    )

    theLegend = ROOT.TLegend(0.6, 0.6, 0.9, 0.9)
    theLegend.AddEntry(unpackedETs, "Unpacked", 'l')
    theLegend.AddEntry(emulatedETs, "Emulated", "l")
    theLegend.SetFillStyle(0)
    theLegend.SetLineWidth(0)

    theLegend.Draw()

    theCanvas.SaveAs(
        str(outputPath/f"{histName}.png")
    )

def makeInputHistograms(eventETs, eventInput, eventNo, modelInputs):
    for iPhi in range(18):
        for iEta in range(14):
            eventETs.Fill(modelInputs[eventNo][iPhi][iEta])
            eventInput.Fill(iEta, iPhi, modelInputs[eventNo][iPhi][iEta])
    return eventETs, eventInput

def main(args):
    ROOT.gStyle.SetOptStat(0)
    #make some TChains, we're not going to overcomplicate this.
    emulatorChain = ROOT.TChain('l1CaloSummaryEmuTree/L1CaloSummaryTree')
    unpackedChain = ROOT.TChain('l1CaloSummaryTree/L1CaloSummaryTree')

    emulatorChain.AddFile(args.fileIn)
    unpackedChain.AddFile(args.fileIn)
    
    nEvents = emulatorChain.GetEntries()
    console.log(f'# of events: {nEvents:>6d}')

    outputPath = Path(args.outputPath)
    outputPath.mkdir(exist_ok=True)

    emulatedScores = ROOT.TH1D(
        'emulated_score',
        'emulated_score',
        30,
        0.0,
        256.0,
    )
    unpackedScores = ROOT.TH1D(
        'unpacked_score',
        'unpacked_score',
        30,
        0.0,
        256.0,
    )

    differenceHist = ROOT.TH1D(
        'score_difference',
        'score_difference',
        20,
        -100.0,
        100.0,
    )
    absDifferenceHist = ROOT.TH1D(
        'abs_score_difference',
        'abs_score_difference',
        20,
        0,
        200.0,
    )

    exampleEmulatedEvent = ROOT.TH2D(
        'exampleEmulatedEvent',
        'exampleEmulatedEvent',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0,
    )
    exampleUnpackedEvent = ROOT.TH2D(
        'exampleUnpackedEvent',
        'exampleUnpackedEvent',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0,        
    )
    exampleEmptyEmulatedEvent = ROOT.TH2D(
        'exampleEmptyEmulatedEvent',
        'exampleEmptyEmulatedEvent',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0,
    )
    exampleEmptyUnpackedEvent = ROOT.TH2D(
        'exampleEmptyUnpackedEvent',
        'exampleEmptyUnpackedEvent',
        14,
        0.0,
        14.0,
        18,
        0.0,
        18.0,        
    )


    simulatedRegionETs = ROOT.TH1D(
        'exampleEmulatedETs',
        'exampleEmulatedETs',
        50,
        0.0,
        50.0,
    )
    unpackedRegionETs = ROOT.TH1D(
        'exampledUnpackedETs',
        'exampledUnpackedETs',
        50,
        0.0,
        50.0,
    )
    simulatedEmptyRegionETs = ROOT.TH1D(
        'exampleEmptyEmulatedETs',
        'exampleEmptyEmulatedETs',
        50,
        0.0,
        50.0,
    )
    unpackedEmptyRegionETs = ROOT.TH1D(
        'exampledEmptyUnpackedETs',
        'exampledEmptyUnpackedETs',
        50,
        0.0,
        50.0,
    )

    emulatorChain.GetEntry(0)
    unpackedChain.GetEntry(0)
    
    for nEvent in track(range(nEvents), description="Events"):
        emulatorChain.GetEntry(nEvent)
        unpackedChain.GetEntry(nEvent)

        emulatedScores.Fill(emulatorChain.CaloSummary.CICADAScore)
        unpackedScores.Fill(unpackedChain.CaloSummary.CICADAScore)

        scoreDifference = emulatorChain.CaloSummary.CICADAScore - unpackedChain.CaloSummary.CICADAScore
        absScoreDifference = abs(scoreDifference)

        differenceHist.Fill(scoreDifference)
        absDifferenceHist.Fill(absScoreDifference)

    #for whatever reason TBranchElement and multidimensional arrays are _impossible_ to read
    #and rife with seg-faulting fun.
    #This is the _only_ method I have found that gives me the ability to read this input into anything comprehensible
    uprootFile = uproot.open(args.fileIn)
    emulatedBranchElement = uprootFile["l1CaloSummaryEmuTree"]["L1CaloSummaryTree"]["CaloSummary"]
    unpackedBranchElement = uprootFile["l1CaloSummaryTree"]["L1CaloSummaryTree"]["CaloSummary"]

    emulatedModelInputs = emulatedBranchElement["modelInput[18][14]"].array()
    unpackedModelInputs = unpackedBranchElement["modelInput[18][14]"].array()
    simulatedRegionETs, exampleEmulatedEvent = makeInputHistograms(simulatedRegionETs, exampleEmulatedEvent, 0, emulatedModelInputs)
    unpackedRegionETs, exampleUnpackedEvent = makeInputHistograms(unpackedRegionETs, exampleUnpackedEvent, 0, unpackedModelInputs)
    
    drawScorePlots(unpackedScores, emulatedScores, outputPath)
    drawScoreDifferencePlot(differenceHist, 'scoreDifference', 'Emulator - Unpacked Score', outputPath)
    drawScoreDifferencePlot(absDifferenceHist, 'absScoreDifference', '|Emulator - Unpacked Score|', outputPath)

    drawEventInput(exampleEmulatedEvent, 'emulatedInput', outputPath)
    drawEventInput(exampleUnpackedEvent, 'unpackedInput', outputPath)

    drawEventETs(unpackedRegionETs, simulatedRegionETs, outputPath)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run tests on L1 added ntuples for Calo Summary checks')
    
    parser.add_argument(
        '--fileIn',
        required=True,
        nargs='?',
        help='File to make plots for'
    )

    parser.add_argument(
        '--outputPath',
        default='./Plots',
       nargs='?',
       help='Path to place plots in'
    )

    args = parser.parse_args()
    
    main(args)
