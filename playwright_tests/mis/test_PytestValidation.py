import pytest


#fixtures

#To use resuable code acrosos the code

@pytest.fixture(scope="module")
def preWork():
    print('this is pre work instance')
    return 'fail'

@pytest.fixture(scope="function")
def secondwork():
    print("this is second work")
    yield
    print("This is after yield statement")

\def test_initialCheck(preWork,secondwork):
    print("This is first test for initial check")
    assert preWork == 'fail'

def test_finalCheck(preWork):
    print("This is last test")