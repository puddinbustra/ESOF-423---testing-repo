import pytest
from mypkg.happy import cake


def test_fib_10():
	assert(cake(10) == 55)
    
