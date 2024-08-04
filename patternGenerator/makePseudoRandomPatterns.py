from utilities import *
from eventObjects import *
from patternObjects import *

import argparse
import numpy as np
from rich.console import Console
from rich.progress import track

from huggingface_hub import from_pretrained_keras

console = Console()

def main(args):
    regionPatterns = RegionPatternCollection()
    scorePatterns = ModelScorePatternCollection()

    model = from_pretrained_keras("cicada-project/cicada-v2.1")

    if args.seed == None:
        seed = np.random.randint(0, 999999)
        rng = np.random.default_rng(seed)
        console.print(f'Using a seed of {seed}')
    else:
        rng = np.random.default_rng(args.seed)
        console.print(f'Using a seed of {args.seed}')

    console.print(f'Making {args.nPatterns} patterns')
    console.print(f'Max: {args.max}, min: {args.min}')
    console.print("Making pseudo random inputs...")
    cicadaInputs = np.random.randint(
        low=args.min,
        high=args.max,
        size=(args.nPatterns, 18, 14)
    )
    console.print("Done!")
    modelInputs = cicadaInputs.reshape((-1, 252))

    console.print('Making predictions...')
    modelPredictions = model.predict(modelInputs)
    console.print("Done!")

    for index in track(range(len(cicadaInputs)), description="Making patterns from results"):
        theEvent = Event()
        theEvent.insertRegionGrid(cicadaInputs[index, :, :,])
        theEvent.modelScore = modelPredictions[index][0]

        regionPatterns.insertEvent(theEvent)
        scorePatterns.insertEvent(theEvent)
        
    regionPatterns.dumpOutPatternCollection()
    scorePatterns.dumpOutPatternCollection()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pseudo random input patterns for CICADA')
    parser.add_argument(
        '-n',
        '--nPatterns',
        default=10240,
        type=int,
        help='Number of patterns to generate'
    )
    parser.add_argument(
        '-s',
        '--seed',
        help='Specify a seed to use to generate patterns with'
    )
    parser.add_argument(
        '--max',
        default=1023,
    )
    parser.add_argument(
        '--min',
        default=0,
    )

    args = parser.parse_args()
    main(args)
