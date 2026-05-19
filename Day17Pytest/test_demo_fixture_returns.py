#Fixture -- Reusable Function which can be used before any test function


import pytest

@pytest.fixture()

def setup():
    print('setup browser...')
    return 'chrome'

def test_one(setup):
    print('this is my test one')
    print('Browser is setup',setup)

def test_two(setup):
    print('this is my test two')
    print('Browser is setup', setup)

def test_three(setup):
    print('This is my test three')
    print('Browser is setup', setup)