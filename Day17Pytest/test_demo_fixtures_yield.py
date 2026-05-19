#Fixture -- Reusable Function which can be used before any test function


import pytest

@pytest.fixture()

def setup():
    print('setup browser...')
    yield
    print('close browser')

def test_one(setup):
    print('this is my test one')

def test_two(setup):
    print('this is my test two')

def test_three(setup):
    print('This is my test three')