# Constructors of Class

Define a class named `Circle` which can be constructed by a radius. The `Circle` class has a method named `area` which can compute the area.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/constructors_of_class.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return round(3.1416*(self.radius**2), 4)


radius = int(input())
circle = Circle(radius)
print(circle.area())

```

This Python code demonstrates how to define a Circle class and calculate the area of a circle. First, a class named `Circle` is defined, which includes a constructor `__init__` and a method `area` to calculate the area of a circle.

In the constructor, an instance variable named `radius` is initialized with the value of the parameter `r` passed to the constructor.

In the `area` method, the area of the circle is calculated using the formula for the area of a circle, and the `round` function is used to round the result to 4 decimal places.

Next, the `input` function is used to read an integer `radius`, and an object named `circle` is created using the `Circle` class with a radius of `radius`.

Finally, the `print` function is used to print the calculated area of the circle to the console.

Overall, this code demonstrates how to define a class, create objects using the class, and define methods in the class to calculate the area of a circle.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/constructors_of_class.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
5
```

Then, the output of the program should be:

```bash
78.54
```

At this point, your code is running successfully!
