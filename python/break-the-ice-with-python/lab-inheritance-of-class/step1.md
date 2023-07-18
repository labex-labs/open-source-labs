# Inheritance of Class

Define a class named `Shape` and its subclass `Square`. The `Square` class has an init function which takes a length as argument. Both classes have a `area` function which can print the area of the shape where `Shape`'s area is 0 by default.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/inheritance_of_class.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length


Asqr = Square(5)
print(Asqr.area())

print(Square().area())

```

This Python code defines a parent class called `Shape` and a child class called `Square`. The `Shape` class has an `area` method that returns 0 by default, and the `Square` class has an `area` method that calculates the area of a square based on its length.

The `Square` class also has an `__init__` method that initializes the length of the square. If no length is provided, the default value of 0 is used.

In the main program, an instance of the `Square` class is created with a length of 5, and its area is calculated and printed to the console using the `print` function.

Another instance of the `Square` class is also created with no length provided, and its area is calculated and printed to the console using the `print` function. Since no length is provided, the default value of 0 is used, and the area of the square is 0.

Overall, this code demonstrates how to use inheritance in Python to create a child class that inherits methods from a parent class, and how to override a method in the child class to provide a different implementation.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/inheritance_of_class.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

The output of the program should be:

```bash
25
0
```

At this point, your code is running successfully!
