# import pytest
# from mypkg.happy import cake


# def test_fib_10():
# 	assert(cake(10) == 10)
    
    
import pytest
from prescriber.tests import travisTest
#from file import function, for example: from prescriber.admin import adminFunction

assert(travisTest(10) == 10)
