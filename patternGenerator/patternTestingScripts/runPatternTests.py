import argparse
import subprocess
from rich.console import Console

console = Console()

def main(args):
    #step 1. prep the inputs
    prepCommand = f'python3 patternTestingScripts/prepDirectoryForPatternTest.py -d {args.directory}'
    prepResults = subprocess.run(
        [prepCommand],
        shell=True,
        #stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if prepResults.returncode != 0:
        console.log('Directory prep step failed.')
        console.log('stderr:')
        console.log(prepResults.stderr.decode())
        exit(prepResults.returncode)
    #step 2. execute the tests on card
    testCommand = f'python3 patternTestingScripts/executeCustomPatternTests.py'
    testResults = subprocess.run(
        [testCommand],
        shell=True,
        #stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if testResults.returncode != 0:
        console.log('Test execution failed.')
        console.log('stderr:')
        console.log(testResults.stderr.decode())
        exit(testResults.returncode)
    #step 3. retrieve the outputs
    retrieveCommand = f'python3 patternTestingScripts/finalizeOutput.py -d {args.directory}'
    retrieveResults = subprocess.run(
        [retrieveCommand],
        shell=True,
        #stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if retrieveResults.returncode != 0:
        console.log('Retrieving results failed.')
        console.log('stderr:')
        console.log(retrieveResults.stderr.decode())
        exit(retrieveResults.returncode)
    #step 4. parse the outputs
    parseCommand = f'python3 patternTestingScripts/parseMultiFileSuccess.py -d {args.directory}'
    if args.verbose:
        parseCommand += ' --verbose'
    parseResults = subprocess.run(
        [parseCommand],
        shell=True,
        #stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if parseResults.returncode != 0:
        console.log('Parsing results failed.')
        console.log('stderr:')
        console.log(parseResults.stderr.decode())
        exit(parseResults.returncode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Main script/single point of contact for running pattern tests from existing patterns')
    parser.add_argument(
        '-d',
        '--directory',
        type=str,
        required=True,
        help='Directory containing inputs and expected outputs to be used in the pattern testing'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Pass verbose information to all related infrastructure'
    )

    args = parser.parse_args()

    main(args)
