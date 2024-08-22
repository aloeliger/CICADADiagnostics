# !/usr/bin/env python3
# run the simple ntuplization config on all the files in a run

import argparse
from rich.console import Console
import subprocess
from pathlib import Path
from step1 import findGoodDataset
from typing import Optional

console = Console()

def getListOfFiles(dataset: str, runNumber: int) -> Optional[list[str]]:
    subProcessCommand = f'dasgoclient --query=\"file dataset={dataset} run={runNumber}\"'
    theProcess = subprocess.run(
        [subProcessCommand],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if theProcess.returncode != 0:
        console.log(f':warning-emoji: [red]File das query failed with error code:[/red] {theProcess.returncode}')
        console.log('Stderr:')
        console.log(theProcess.stderr.decode())
        console.log('Returning none')
        return None

    dasQueryOutput = theProcess.stdout.decode()
    dasQueryOutput = dasQueryOutput.split('\n')
    dasQueryOutput = dasQueryOutput[:-1] # last entry is always empty

    return dasQueryOutput

def runNtuples(listOfFiles: list[str]) -> None:
    subprocessCommand = f'cmsRun RunEmulatorNtuples.py inputFiles='+','.join(listOfFiles)+' outputFile=file:./L1Ntuple.root'

    theProcess=subprocess.run(
        [subprocessCommand],
        shell=True,
    )

    if theProcess.returncode != 0:
        console.log(f':warning-emoji: [red]Failed to run the cmsRun configuration with all files[/red]')
        return None

def main(args) -> None:
    console.log(f'Finding appropriate dataset')
    recommendedDataset = findGoodDataset(args.runNumber)
    if recommendedDataset == None:
        console.log(':warning-emoji: Could not find a dataset for this run number. Quitting.', style='red')
        exit(1)
    console.log(f':white_check_mark-emoji: [green]Found recommended dataset:[/green] {recommendedDataset}')

    listOfFiles = getListOfFiles(recommendedDataset, args.runNumber)
    if listOfFiles == None:
        console.log(':warning-emoji: Could not get a full list of files for this run number and dataset. Quitting.', style='red')
        exit(1)
    console.log(':white_check_mark-emoji: [green]Got complete list of files[/green]')
    console.print(f'Number of files in run: {len(listOfFiles)}')

    console.log('Running all ntuples')
    runNtuples(listOfFiles)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Quickly ntuplize an entire runs worth of CICADA info')

    parser.add_argument(
        '--runNumber',
        type=int,
        nargs='?',
        help='Run number to Ntuplize',
    )

    args = parser.parse_args()

    main(args)
    
