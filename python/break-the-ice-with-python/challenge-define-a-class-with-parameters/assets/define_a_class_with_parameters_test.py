import sys
import importlib.util
import unittest

sys.path.append("/home/labex/project")


class TestCar(unittest.TestCase):
    def test_car_class(self):
        # Load the module
        spec = importlib.util.spec_from_file_location(
            "Car", "/home/labex/project/define_a_class_with_parameters.py"
        )
        car = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(car)

        # Check if the class exists
        if hasattr(car, "Car"):
            Car = getattr(car, "Car")
            # Check if the class has a name class attribute
            if hasattr(Car, "name"):
                # Check if the class has a name instance attribute
                car_instance = Car()
                if hasattr(car_instance, "name"):
                    self.assertEqual(
                        Car.name, "Car", "The class has a name class attribute."
                    )
                    self.assertIsNone(
                        car_instance.name, "The class has a name instance attribute."
                    )
                else:
                    self.fail("The class does not have a name instance attribute.")
            else:
                self.fail("The class does not have a name class attribute.")
        else:
            self.fail("The class does not exist in the module.")


if __name__ == "__main__":
    unittest.main()
