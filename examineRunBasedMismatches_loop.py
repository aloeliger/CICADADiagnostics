import ROOT
import argparse
from rich.console import Console
from rich.progress import track
from pathlib import Path
import numpy as np
import termplotlib
from time import perf_counter

console = Console()

def main(args):
    fileDirectory = Path(args.fileDir)

    allFiles = list(fileDirectory.rglob('*.root'))
    allFiles = [str(x) for x in allFiles]

    emulatorEventChain = ROOT.TChain('l1EventTree/L1EventTree')
    emulatorChain = ROOT.TChain('l1CaloSummaryEmuTree/L1CaloSummaryTree')

    unpackedEventChain = ROOT.TChain('l1EventTree/L1EventTree')
    unpackedChain = ROOT.TChain('l1CaloSummaryTree/L1CaloSummaryTree')    

    for fileName in track(allFiles, description='Adding files'):
        emulatorEventChain.AddFile(fileName)
        emulatorChain.AddFile(fileName)

        unpackedEventChain.AddFile(fileName)
        unpackedChain.AddFile(fileName)

    emulatorChain.AddFriend(emulatorEventChain)
    unpackedChain.AddFriend(unpackedEventChain)
    
    start_time = perf_counter()
    totalEntries = unpackedChain.GetEntries()
    end_time = perf_counter()
    console.print(f'Total Events: {int(totalEntries)} (calculated in {end_time-start_time:4.2g} seconds)')
    console.print(f'Using 1 out of every {args.skipFactor} event(s)')

    totalEvents = {}
    mismatches = {}

    nonZeroEventsMatches = {}
    nonZeroEvents = {}
    
    noMismatchEvents = 0

    for i in track(range(totalEntries), description='Looping events'):
        if i % args.skipFactor != 0:
            continue
        unpackedChain.GetEntry(i)
        emulatorChain.GetEntry(i)

        run = int(unpackedChain.GetLeaf("run").GetValue())
        #DEBUG
        if run != 383162:
            continue

        event = int(unpackedChain.GetLeaf("event").GetValue())
        if run not in totalEvents:
            totalEvents[run] = 0
        totalEvents[run] += 1
        if run not in mismatches:
            mismatches[run] = 0
        if run not in nonZeroEventsMatches:
            nonZeroEventsMatches[run] = 0
        if run not in nonZeroEvents:
            nonZeroEvents[run] = 0

        unpackedScore = unpackedChain.GetLeaf("CICADAScore").GetValue()
        emulatorScore = emulatorChain.GetLeaf("CICADAScore").GetValue()


        discrepancy = emulatorScore - unpackedScore
        #DEBUG
        console.print(f'Run: {run}, Event: {event}, unpacked score: {unpackedScore}, emulator score: {emulatorScore}, discrepancy: {discrepancy}')

        if discrepancy != 0.0:
            mismatches[run] += 1
        else:
            noMismatchEvents += 1

        if emulatorScore != 0.0:
            nonZeroEvents[run] += 1
            if discrepancy == 0.0:
                nonZeroEventsMatches[run] += 1
        

    for key in totalEvents:
        display_nonZeroEvents = nonZeroEvents[key]
        display_nonZeroEventsMatches = nonZeroEventsMatches[key]
        try:
            nonZeroMatchPercent = display_nonZeroEventsMatches / display_nonZeroEvents
        except ZeroDivisionError:
            nonZeroMatchPercent = 0.0
        console.print(f'Run: {key}, mismatches: {mismatches[key]:<9}/{totalEvents[key]:>9}, {mismatches[key]/totalEvents[key]:05.2%}, non-zero emulator score matches: {nonZeroEventsMatches[key]:<9}/{nonZeroEvents[key]:>9}, {nonZeroMatchPercent:05.2%}')
    console.print(f'Number of events with emulator-firmware agreement: {noMismatchEvents}')

    mismatch_fractions = []
    mismatch_runs = []
    for key in totalEvents:
        mismatch_runs.append(key)
        mismatch_fractions.append(
            mismatches[key] / totalEvents[key]
        )

    mismatch_fig = termplotlib.figure()
    mismatch_fig.barh(
        mismatch_fractions,
        mismatch_runs,
    )
    mismatch_fig.show()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Examine as many runs as possible, looking for mismatched emulator/DAQ CICADA scores')

    parser.add_argument(
        '--fileDir',
        required=True,
        nargs='?',
        help='Directory to search for files'
    )
    parser.add_argument(
        '--skipFactor',
        default=1,
        type=int,
        help='Factor of events to skip'
    )

    args = parser.parse_args()

    main(args)
