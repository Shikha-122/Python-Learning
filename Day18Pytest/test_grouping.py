'''

grouping tests:
----------
test_LoginByEmail -> sanity,regression
test_LoginByFacebook -> sanity
test_LoginByPhone --> regression
test_signupByEmail --> sanity,regression
test_signupByFacebook --> regression
test_signupByPhone --> sanity
test_paymentInDollar -> sanity, regression
test_paymentInRupees -> regression

'''

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    print('This is login by email test')
    assert 1==1

@pytest.mark.sanity
def test_loginbyfacebook():
    print('This is login by facebook test')
    assert 1 == 1

@pytest.mark.regression
def test_loginbyphone():
    print('This is login by phone test')
    assert 1 == 1

@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyemail():
    print('This is signup by email test')
    assert 1==1

@pytest.mark.regression
def test_signupbyfacebook():
    print('This is signup by facebook test')
    assert 1 == 1

@pytest.mark.sanity
def test_signupbyphone():
    print('This is signup by phone test')
    assert 1 == 1

@pytest.mark.sanity
@pytest.mark.regression
def test_paymentInDollar():
    print('This is payment in dollar test')
    assert 1==1

@pytest.mark.regression
def test_paymentInRupees():
    print('This is payment in rupess test')
    assert 1==1

'''
1) run sanity tests (5)
       pytest day18Pytest/test_grouping.py -s -v -m 'sanity'

2) run only regression tests (6)
       pytest Day18Pytest/test_grouping.py -s -v -m 'regression'

3) run tests which belongs to both sanity regression (3)
       pytest Day18Pytest/test_grouping.py -v -s -m ' sanity and regression'
       
4) run only sanity tests which are not belongs to regression
        pytest Day18Pytest/test_grouping.py -s -v -m 'sanity' -m 'not regression'
        
5) run only regression tests which are not belongs to sanity
        pytest Day18Pytest/test_grouping.py -s -v -m 'regression' -m 'not sanity'
'''
