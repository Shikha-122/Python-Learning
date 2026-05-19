'''

pre-requisite : install pytest-order plugin
     pip  install pytest-order #latest
'''

import pytest

#Approach 1 : order tests by position

# @pytest.mark.order(3)
# def test_login():
#     print('this is login test')
#
# @pytest.mark.order(1)
# def test_add_item():
#     print('this is add item test')
#
# @pytest.mark.order(2)
# def test_logout():
#     print('this is logout')

# Approach 2 using before , after

# @pytest.mark.order(after='test_add_item')
# def test_checkout():
#     print('this is checkout test')
#
# @pytest.mark.order(after='test_login')
# def test_add_item():
#     print('this is add item test')
#
# @pytest.mark.order(1)
# def test_login():
#     print('this is login test')

# Approach 3 : using marker strings (user defined)



@pytest.mark.order('second')
def test_add_item():
    print('this is add item test')

@pytest.mark.order('third')
def test_checkout():
    print('this is checkout test')

@pytest.mark.order('first')
def test_login():
    print('this is login test')


