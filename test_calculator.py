from calculator import add, subtract

class TestCalculator:
    def test_add(self):
        assert add(2, 3) == 5

    def test_subtract(self):
        assert subtract(10, 4) == 6
