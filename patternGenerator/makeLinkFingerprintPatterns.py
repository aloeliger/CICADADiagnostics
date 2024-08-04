from utilities import *
from eventObjects import *
from patternObjects import *

import argparse
import numpy as np
import itertools
from rich.console import Console
from rich.progress import track

from huggingface_hub import from_pretrained_keras

def main(args):
    regionPatterns = RegionPatternCollection()
    scorePatterns = ModelScorePatternCollection()

    model = from_pretrained_keras("cicada-project/cicada-v2.1")
    
    regionSaturationValue = 1023
    for linkNo in track(range(36), description='links'):
        cicadaInput = np.zeros((18,14))
        if linkNo % 2 == 0:
            etas = [0, 1, 2, 3, 4, 5, 6]
        else:
            etas = [7, 8, 9, 10, 11, 12, 13]
        iPhi = linkNo // 2
        for index, iEta in enumerate(etas):
            cicadaInput[iPhi][iEta] = regionSaturationValue

        modelInput = cicadaInput.reshape((252,)).reshape((1,252))

        prediction = model.predict(modelInput, verbose=0)

        theEvent = Event()
        theEvent.insertRegionGrid(cicadaInput)
        theEvent.modelScore = prediction

        regionPatterns.insertEvent(theEvent)
        scorePatterns.insertEvent(theEvent)

    regionPatterns.dumpOutPatternCollection()
    scorePatterns.dumpOutPatternCollection()
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make link saturating patterns')

    args = parser.parse_args()

    main(args)
