import pytest

@pytest.fixture
def before():
    print('      before')
    yield None
    print('      after')

@pytest.fixture(params=[1,2])
def return_value(request):
    print('      return_value')
    return 3.14*request.param

def test_this(before):
    print('            ', end='')

def test_that(return_value):
    print('            ', end='')
    print(return_value, end='')