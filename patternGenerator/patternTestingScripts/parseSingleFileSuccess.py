import argparse
import pathlib
import re
from rich.console import Console
from rich.table import Table

console = Console()

class fileContents():
    def __init__(self, fileObj):
        self.fileObj = fileObj
        self.contents = self.fileObj.readlines()
        self.contents = self.contents[3:] # skips the first three header lines 
        
        self.events = [self.contents[i:i+6] for i in range(0, len(self.contents), 6)] # we expect 6 lines per event, this splits the lines up into distinct events
        self.parseEventsToCICADAWords()

    def parseEventsToCICADAWords(self):
        self.CICADAWords = []
        for event in self.events:
            cicadaWord = ''
            for line in event[:4]: #we expect CICADA in the first 4 lines of the words
                cicadaDigit = re.search('(?<=\s0x)[0-9a-f](?=[0-9A-Fa-f]{7})', line)
                if not cicadaDigit:
                    console.log('Failed to find CICADA digit in line:')
                    console.log(line)
                    exit(1)
                cicadaDigit = cicadaDigit.group(0)
                cicadaWord += cicadaDigit
            self.CICADAWords.append(cicadaWord)
    @property
    def size(self):
        return len(self.CICADAWords)
            

def compareFileContentEquality(expectedContents, receivedContents, verbose=False):
    matches = []
    fileMatch = True
    if expectedContents.size != receivedContents.size:
        if verbose:
            console.log('Received different sized file contents')
            console.log('Expected contents size: ', len(expectedContents.CICADAWords))
            console.log('Received contents size: ', len(receivedContents.CICADAWords))
        if expectedContents.size < receivedContents.size:
            if verbose:
                console.log('Shrinking received to match')
            receivedContents.CICADAWords = receivedContents.CICADAWords[:expectedContents.size]
        elif receivedContents.size < expectedContents.size:
            if verbose:
                console.log('Shrinking expected to match')
            expectedContents.CICADAWords = expectedContents.CICADAWords[:receivedContents.size]
    
    for index in range(expectedContents.size):
        if expectedContents.CICADAWords[index] != receivedContents.CICADAWords[index]:
            fileMatch =  False
            matches.append(False)
        else:
            matches.append(True)

    infoTable = Table(title='Patterns')
    infoTable.add_column('Pattern #')
    infoTable.add_column('Expected word')
    infoTable.add_column('Received word')
    infoTable.add_column('Match?')
    for index in range(len(matches)):
        if matches[index] == True:
            matchStr = "[black on green]True[/black on green]"
        else:
            matchStr = "[black on red]False[/black on red]"
        infoTable.add_row(
            f'{index}',
            expectedContents.CICADAWords[index],
            receivedContents.CICADAWords[index],
            matchStr
        )

    if verbose:
        console.print(infoTable)
        console.print(f'File matches? {fileMatch}')
    return fileMatch
            
def runComparison(expectedOutput, receivedOutput, verbose):
    with open(expectedOutput) as theFile:
        expectedFileContents = fileContents(theFile)

    with open(receivedOutput) as theFile:
        receivedFileContents = fileContents(theFile)

    fileMatch = compareFileContentEquality(expectedFileContents, receivedFileContents, verbose)
    if fileMatch:
        return 0
    else:
        return 1


def main(args):
    if args.verbose:
        console.print(f'Checking CICADA output contents for {args.expectedOutput}')
    returnCode = 0
    #this feels a little weird. This maybe should be reworked.
    #Maybe don't force the file contents object to keep the file object around?
    expectedOutput = pathlib.Path(args.expectedOutput)
    receivedOutput = pathlib.Path(args.receivedOutput)

    returnCode = runComparison(expectedOutput, receivedOutput, args.verbose)
    return returnCode
        
if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="Compare two corresponding pattern test output files to figure out if there are any disagreements")
    parser.add_argument(
        '--expectedOutput',
        required=True,
        help='Emulator based output expected words',
        type=str,
    )
    parser.add_argument(
        '--receivedOutput',
        required=True,
        help='FPGA output received words',
        type=str,
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print details about individual file matches and mismatches'
    )

    args = parser.parse_args()

    returnCode = main(args)
    exit(returnCode)
