import sys
import pytest

sys.path.insert(0, 'ESOF-423\tests')

def testHappy():
    assert(happy(10) == 55)
    
