# !/usr/bin/env python3
# Script designed to take a run number to check
# From there it should identify an appropriate dataset and file on DAS
# Then it will make a FED dump (for 10 events) + L1T Ntuple (all)

import argparse
from rich.console import Console
import subprocess
from pathlib import Path
import datetime

console = Console()

# Once we have a list of datasets, select one
# Our algorithm will be simple. Simply select one that is zero bias or minimum bias
# Return none if we can't find one like that
def parseDatasetList(theList: list[str]):
    for entry in theList:
        if 'ZeroBias' in entry or 'MinimumBias' in entry:
            return entry

    return None

# Come up with a recommended dataset to find a file from given the run number
def findGoodDataset(runNumber: int):
    subProcessCommand = f'dasgoclient --query=\"dataset run={runNumber} tier=RAW\"'
    theProcess = subprocess.run(
        [subProcessCommand],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if theProcess.returncode != 0:
        console.log(f":warning-emoji: [red]Dataset das query failed with error code:[/red] {theProcess.returncode}")
        console.log("Returning none")
        return None

    dasQueryOutput = theProcess.stdout.decode()
    dasQueryOutput = dasQueryOutput.split('\n')
    dasQueryOutput = dasQueryOutput[:-1]

    recommendation = parseDatasetList(dasQueryOutput)
    
    return recommendation

# run through the list of files we have just found
# if we can find one that isn't on tape, we can just use that.
def checkForGoodFile(listOfFiles):
    for fileName in listOfFiles:
        subProcessCommand = f'dasgoclient --query=\"site file={fileName}\"'
        theProcess = subprocess.run(
            [subProcessCommand],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if theProcess.returncode != 0:
            console.log(f':warning-emoji: [red]Das query to determine site of file {fileName} failes with return code:[/red] {theprocess.returncode}\nContinuing to next file.')
            continue
        sites = theProcess.stdout.decode().split('\n')[:-1]
        for site in sites:
            if 'tape' not in site.lower():
                return fileName
    return None

def findRecommendedFile(dataset, runNumber):
    subProcessCommand = f'dasgoclient --query=\"file dataset={dataset} run={runNumber}\"'
    theProcess = subprocess.run(
        [subProcessCommand],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if theProcess.returncode != 0:
        console.log(f":warning-emoji: [red]File das query failed with error code:[/red] {theProcess.returncode}")
        console.log('Returning none')
        return None

    dasQueryOutput = theProcess.stdout.decode()
    dasQueryOutput = dasQueryOutput.split('\n')
    dasQueryOutput = dasQueryOutput[:-1]

    recommendedFile = checkForGoodFile(dasQueryOutput)

    return recommendedFile

def makeFEDDump(recommendedFile, outputDirectory):
    fedDumpCommand = f'cmsRun fedDumpingTool/dumpFEDInfoFromRAW.py feds=1356,1405 inputFiles={recommendedFile} -n 10'
    theProcess = subprocess.run(
        [fedDumpCommand],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if theProcess.returncode != 0:
        console.log(f':warning-emoji: [red]FED Dump command failed with exit code:[/red] {theProcess.returncode}')
        console.log('Returning false')
        return False
    
    fedDump = theProcess.stderr.decode()
    with open(outputDirectory/'FEDDump.log', 'w+') as theFile:
        theFile.write(fedDump)
    
    return True

def makeL1Ntuple(recommendedFile, outputDirectory):
    cmsDriverCommand = f'cmsDriver.py L1Ntuples -s RAW2DIGI,L1 --era=Run3 --data --conditions=auto:run3_data --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW,L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMU -n -1 --filein={recommendedFile} --fileout=file:./test.root'
    theProcess = subprocess.run(
        [cmsDriverCommand],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if theProcess.returncode != 0:
        console.log(f':warning-emoji: [red]L1Ntuple creation process faile with exit code:[/red] {theProcess.returncode}')
        return False

    #We don't need to decode any of the input to this, we can just move the final file into the output
    finalL1Ntuple = Path('./L1Ntuple.root')
    finalL1Ntuple.rename(outputDirectory/'L1Ntuple.root')

    outputFile = Path('./test.root')
    outputFile.rename(outputDirectory/'test.root')

    configFile = Path('./L1Ntuples_RAW2DIGI_L1.py')
    configFile.rename(outputDirectory/'L1Ntuples_RAW2DIGI_L1.py')
    return True

def main(args):
    #First step. Try and find a dataset for this run.
    #If we can't find it, we're done there, and error out
    recommendedDataset = findGoodDataset(args.runNumber)
    if recommendedDataset == None:
        console.log(':warning-emoji: Could not find a dataset for this run number. Quitting.', style='red')
        exit(1)
    console.log(f':white_check_mark-emoji: [green]Found recommended dataset:[/green] {recommendedDataset}')
    
    # Second step. Now we go and find a file we can use
    recommendedFile = findRecommendedFile(recommendedDataset, args.runNumber)
    if recommendedDataset == None:
        console.log(':warning-emoji: Could not find a file for this run number. Quitting.', style='red')
        exit(1)
    console.log(f':white_check_mark-emoji: [green]Found recommended file:[/green] {recommendedFile}')

    # Third step. Set-up a directory we can use to store out output
    if args.outputDirectory == None:
        dateTimeStr = datetime.datetime.now().strftime('%b_%d_%Y_%H_%M')
        outputDirectory = f'./Run{args.runNumber}_{dateTimeStr}'
        outputDirectory = Path(outputDirectory)
    else:
        outputDirectory = Path(args.outputDirectory)
        
    try:
        outputDirectory.mkdir()
    except:
        console.log(f':warning-emoji: Failed to make output directory: {outputDirectory}\n Quitting.', style=red)
        exit(1)
    else:
        console.log(f':white_check_mark-emoji: [green]Made output directory:[/green] {outputDirectory}')

    # Fourth step. We make FED dumps of this file for ten events
    FEDDumpSucceeded = makeFEDDump(recommendedFile, outputDirectory)
    if not FEDDumpSucceeded:
        console.log(f':warning-emoji: Failed to make FED Dump. Quitting.', style='red')
        exit(1)
    console.log(f':white_check_mark-emoji: Made FED Dump (10 Events).', style='green')
    
    # Fifth step. We make L1Ntuples of this file
    L1NtupleSucceeded = makeL1Ntuple(recommendedFile, outputDirectory)
    if not L1NtupleSucceeded:
        console.log(f':warning-emoji: Failed to make L1 ntuples. Quitting.', style='red')
        exit(1)
    console.log(f':white_check_mark-emoji: Made L1 Ntuple.', style='green')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a full set of CICADA diagnostics for a given run")

    parser.add_argument(
        '--runNumber',
        type=int,
        nargs='?',
        help='Run number to try and find a suitable file for',
        required=True
    )
    parser.add_argument(
        '--outputDirectory',
        type=str,
        nargs='?',
        help='Directory to store any script output in',
    )

    args = parser.parse_args()
    main(args)
