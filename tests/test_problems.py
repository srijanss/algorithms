from pytest import fixture, raises

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
    assert obj.day_three() == 'left.left'

####################
# Pytest tutorials
####################
def test_answer(obj):
    assert obj.func(3) == 4

def test_f(obj):
    with raises(SystemExit):
        obj.f()

def test_myfunc(obj):
    with raises(ValueError, match=r'.* 123 .*'):
        obj.myfunc()

def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0, "no tmpdir provided"

class Person(object):
    age = 34
    name = 'Admin'

class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = Person()
        assert hasattr(x, 'age')

    def test_three(self):
        with raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
            pass

    def test_set_comparision(self):
        set1 = set("1208")
        set2 = set("8035")
        assert set1 == set2

@fixture(scope='function')
def smtp_connection():
    import smtplib
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection
    print('teardown smtp')
    smtp_connection.close()

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0


@fixture(scope="session")
def s1():
    pass

@fixture(scope="module")
def s2():
    pass

@fixture
def s3(tmpdir):
    pass

@fixture
def s4():
    pass

def test_foo(s4, s3, s2, s1):
    pass

# Monkey Patching
import os.path
def getssh():
    return os.path.join(os.path.expanduser('~admin'), '.ssh')

def test_mytest(monkeypatch):
    def mockreturn(path):
        return '/abc'
    monkeypatch.setattr(os.path, 'expanduser', mockreturn)
    x = getssh()
    assert x == '/abc/.ssh'
