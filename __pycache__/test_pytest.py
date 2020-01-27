import sys
import pytest

sys.path.append('../')

from Rock_Paper_Scissors_Functional import determine_winner

def test_determine_winner ():

    #determine = Rock_Paper_Scissors_Functional()

    #result = determine.determine_winner ("rock","paper")

    assert determine_winner("rock", "paper") == True 