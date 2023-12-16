import unittest
from country import Country
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person(age=20, height=180, sex=True, weight=70, name="John")

    def test_is_alco_buyer(self):
        country = Country("SomeCountry", age_for_alco=18)
        assert self.person.is_alco_buyer(country) is True

    def test_is_non_alco_buyer(self):
        country = Country("SomeCountry", age_for_alco=21)
        assert self.person.is_alco_buyer(country) is False

    def test_get_imt(self):
        self.assertAlmostEqual(self.person.get_imt(), 2.57, places=2)


if __name__ == '__main__':
    unittest.main()
