import unittest
import sys
from io import StringIO
from class_inheritance import Person, Male, Female

class TestPerson(unittest.TestCase):
    def test_person(self):
        # Create a Person object and check its gender
        person = Person()
        self.assertEqual(person.getGender(), "Unknown")

    def test_male(self):
        # Create a Male object and check its gender
        male = Male()
        self.assertEqual(male.getGender(), "Male")

    def test_female(self):
        # Create a Female object and check its gender
        female = Female()
        self.assertEqual(female.getGender(), "Female")

if __name__ == '__main__':
    # Add the path to the project directory
    sys.path.append("/home/labex/project")

    unittest.main()
