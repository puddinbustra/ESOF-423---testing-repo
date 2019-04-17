import pytest
# from mypkg.happy import cake
from django.test import TestCase

# def test_fib_10():
# 	assert(cake(10) == 10)


from prescriber.happy import travisTest

#from file import function, for example: from prescriber.admin import adminFunction
def test_nonsense():
    assert(travisTest(10) == 10)
