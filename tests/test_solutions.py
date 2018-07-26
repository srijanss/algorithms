from pytest import fixture

@fixture
def obj():
    from algorithms.solutions import Solutions
    return Solutions()

def setup_function():
    pass

def teardown_function():
    pass

def test_sieve_algorithm(obj):
    assert obj.sieve_algorithm(10)[0] == False
    assert obj.sieve_algorithm(10)[3] == False
    assert len(obj.sieve_algorithm(1000)) == 1000
