# Execute pattern tests for custom patterns, one at a time
import argparse
import pathlib
from rich.console import Console
from rich.progress import track
import subprocess

console = Console()

def executePatternTest(fileName):
    #Let's figure out what the name of the file is
    #Then we generate an output file name based on what that should be
    #Then, let's actually ssh to krieger and make it run the test
    filePath = pathlib.Path(fileName)
    filePlusSuffix = filePath.stem + filePath.suffix
    fileStem = filePath.stem
    outputFileName = fileStem+'_output.txt'

    ssh_command = f'ssh -t krieger \"cd /cms/aloeliger/anomalyTriggerWork/comissioningCode/CMSSW_14_1_0_pre5/src/CICADADiagnostics/patternGenerator/patternTesting/ && source env.sh && source pattern_test.sh custom_patterns/{filePlusSuffix} {outputFileName}\"'
    
    processResult = subprocess.run(
        [ssh_command],
        shell=True,
        #check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if processResult.returncode != 0:
        console.log(f'SSH command to krieger for pattern tests failed.')
        console.log('Std err of failed attempt:')
        console.log(processResult.stderr.decode())
        exit(1)

def main(args):
    #first things first, let's get a list of the files we're going to run pattern tests for
    customPatternDirectory = pathlib.Path('patternTesting/data/custom_patterns')
    patternFiles = list(customPatternDirectory.glob('*.txt'))
    with console.status('Running pattern tests...'):
        for fileName in patternFiles:
            console.log(f'Running pattern test for file: {fileName}')
            executePatternTest(fileName)
    #for fileName in track(patternFiles, description='Pattern tests'):
    #    executePatternTest(fileName)
    console.print(f'Running pattern tests... [bold green]Done![/bold green]')
    

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Script for pattern tests on the contents of the custom_patterns directory')

    args = parser.parse_args()
    main(args)
