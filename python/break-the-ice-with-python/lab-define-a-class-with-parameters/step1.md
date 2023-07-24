# Define a Class with Parameters

Define a class named `Car`, which have a class parameter named `name` and have a same instance parameter.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/define_a_class_with_parameters.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class Car:
    name = "Car"

    def __init__(self, name=None):
        self.name = name


honda = Car("Honda")
print("%s name is %s" % (Car.name, honda.name))

toyota = Car()
toyota.name = "Toyota"
print("%s name is %s" % (Car.name, toyota.name))

```

This Python code defines a class called `Car`, which contains a class variable `name` and a constructor function `__init__`. The constructor function takes an optional parameter `name` and stores it in an instance variable `name`.

In the main program, an instance of the `Car` class called `Honda` is created, and its `name` attribute is set to "Honda". Then, a string is printed using the `print` function, which contains the values of the class variable `name` and the instance variable `name`.

Next, an instance of the `Car` class called `Toyota` is created, and its `name` attribute is set to "Toyota". Then, another string is printed using the `print` function, which contains the values of the class variable `name` and the instance variable `name`.

Overall, this code demonstrates how to define a class and define class variables and a constructor function within it. It also shows how to use instances of a class to set and get the values of instance variables, and how to use the `print` function to output these values to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/define_a_class_with_parameters.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
Car name is Honda
Car name is Toyota
```

At this point, your code is running successfully!
