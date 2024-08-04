import argparse
import pathlib
import subprocess
from rich.console import Console
from rich.table import Table
from parseSingleFileSuccess import runComparison

console = Console()

def makeFileResults(fileName, expectedOutputPath, receivedOutputPath, verbose):
    filePath = pathlib.Path(fileName)
    fileSucceeded = True

    expectedFilePath = filePath
    receivedFilePath = receivedOutputPath / (filePath.stem + filePath.suffix)

    if not expectedFilePath.exists():
        console.log("Couldn't find expected results file: {expectedFilePath}")
        exit(1)
    if not receivedFilePath.exists():
        console.log("Couldn't find received results file: {receivedFilePath}")
        exit(1)

    returnCode = runComparison(expectedFilePath, receivedFilePath, verbose)

    if returnCode == 1:
        fileSucceeded = False
    elif returnCode != 0 and processResult.returncode != 1:
        console.log("Got unexpected return code from single file success parser")
        console.log("stderr:")
        console.log(processResult.stderr.decode())

    return fileSucceeded

def main(args):
    console.print(f'Comparing results from directory: {args.directory}')
    testVectorDir = pathlib.Path(args.directory)

    expectedOutputPath = testVectorDir / 'outputs'
    receivedOutputPath = testVectorDir / 'received_outputs'

    expectedOutputFiles = list(expectedOutputPath.glob("*.txt"))

    fileSuccesses = []
    processedFiles = []
    allFilesSucceeded = True
    with console.status('Comparing files...'):
        for fileName in expectedOutputFiles:
            fileSucceeded = makeFileResults(fileName, expectedOutputPath, receivedOutputPath, args.verbose)
            if not fileSucceeded:
                allFilesSucceeded = False
            fileSuccesses.append(fileSucceeded)
            processedFiles.append(fileName)
            #console.print(f'Finished with {fileName}. Match? {fileSucceeded}')

    #Okay, let's make a summary table
    infoTable = Table(title="Pattern file matches")
    infoTable.add_column("File #")
    infoTable.add_column("Expected output file path")
    infoTable.add_column("Match?")
    for index in range(len(fileSuccesses)):
        if fileSuccesses[index] == True:
            matchStr = "[black on green]True[/black on green]"
        else:
            matchStr = "[black on red]False[/black on red]"
        infoTable.add_row(
            f'{index}',
            f'{processedFiles[index]}',
            matchStr
        )
    console.print(infoTable)
    console.print(f'All files match? {allFilesSucceeded}')
    console.print("Done!")
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare the complete extracted results of a test vector file')
    parser.add_argument(
        '-d',
        '--directory',
        required=True,
        help='Directory to check expected versus recceived results',
        type = str,
    )
    parser.add_argument(
        '--verbose',
        help='Pass verbose results to any related infrastructure',
        action='store_true',
    )

    args = parser.parse_args()
    
    main(args)
