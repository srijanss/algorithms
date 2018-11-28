from pytest import fixture

@fixture
def obj():
    from dailyproblems.problems import Problems
    return Problems()

def setup_function():
    pass

def teardown_function():
    pass

def test_day_one(obj):
    assert obj.day_one([10, 2, 3, 4, 7], 17) == True
    assert obj.day_one([10, 2, 3, 4, 7], 15) == False 
    assert obj.day_one([1, 2, 3, 4, 5], 5) == True
    assert obj.day_one([1, 2, 3, 5, 5], 10) == True

def test_day_two(obj):
    assert obj.day_two([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert obj.day_two([4, 1, 6, 3, 2]) == [36, 144, 24, 48, 72]

def test_day_three(obj):
    assert obj.day_three() == 'test'
