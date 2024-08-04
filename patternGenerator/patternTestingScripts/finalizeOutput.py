import argparse
import pathlib
import shutil
from rich.console import Console
from rich.progress import track

console = Console()

def retrieveFile(fileName, patternTestingDirectory, directory):
    filePath = pathlib.Path(fileName)
    fileStem = filePath.stem
    outputFileName = fileStem+'_output.txt'
    outputFilePath = patternTestingDirectory / outputFileName

    shutil.move(outputFilePath, directory)

def main(args):
    console.print(f'Extracting pattern test results to: {args.directory}')
    patternTestingDirectory = pathlib.Path('patternTesting/data/')
    originalDirectory = pathlib.Path(args.directory)
    newResultsDirectory = originalDirectory/"received_outputs"
    newResultsDirectory.mkdir()

    inputFiles = list((originalDirectory/"inputs").glob("*.txt"))
    for fileName in track(inputFiles, description="retrieving files"):
        retrieveFile(fileName, patternTestingDirectory, newResultsDirectory)
    console.print('Done!')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A small script to finalize the output of pattern tests, and move them back to the directory containing orignal inputs')
    parser.add_argument(
        '-d',
        '--directory',
        type = str,
        required=True,
        help='Directory containing existing inputs and outputs to move the final outputs back to for comparison',
    )

    args = parser.parse_args()

    main(args)
