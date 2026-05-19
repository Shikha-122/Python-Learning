#Fixture: Re-usable Function

# scope='function' fixture will be called before every test function executes
# scope='modules'  fixture will be called only once before test function executes.
# scope='class'    fixture will be called only once before the class
# scope='session'  fixture will be called only once for session

# module ---> class ---> function
# module ---> function

import pytest

@pytest.fixture

def setup(scope='module'):
    print('setup browser...')

def test_one(setup):
    print('this is my test one')

def test_two(setup):
    print('this is my test two')

def test_three(setup):
    print('This is my test three')