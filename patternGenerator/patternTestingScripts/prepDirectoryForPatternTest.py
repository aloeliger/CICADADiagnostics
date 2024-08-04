# a small script to run as part of the greater pattern testing system
import argparse
import pathlib
import shutil
from rich.console import Console

console = Console()

def main(args):
    console.print(f"Preparing {args.directory} for pattern testing...")
    patternTestingDataDirectory = pathlib.Path('patternTesting/data/custom_patterns/')
    #if this already exists, lets clean it out
    if patternTestingDataDirectory.exists():
        console.print("Found existing patterns in the data directory. Removing.")
        shutil.rmtree(patternTestingDataDirectory)
    #     oldPatternDirectory = pathlib.Path('patternTesting/data/old_patterns')
    #     patternTestingDataDirectory.rename(oldPatternDirectory)
    patternTestingDataDirectory.mkdir(exist_ok=True)

    baseDirectory = pathlib.Path(args.directory)
    inputsDirectory = baseDirectory / 'inputs'
    testFiles = list(inputsDirectory.glob('*.txt'))

    with console.status("Copying files..."):
        for fileName in testFiles:
            shutil.copy(fileName, patternTestingDataDirectory)
    console.print("Copying files... [bold green]Done![/bold green]")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A small script to take an input directory and place the inputs in the pattern testing directory')
    parser.add_argument(
        '-d',
        '--directory',
        type=str,
        required=True,
        help='Directory containing the inputs to be used in the pattern testing',
    )

    args = parser.parse_args()

    main(args)
