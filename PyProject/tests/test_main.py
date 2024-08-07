from src.main import add_numbers

def test_main():
    assert 10 == add_numbers(5,5)

def test_main_wrong():
    assert 10 != add_numbers(10,10)