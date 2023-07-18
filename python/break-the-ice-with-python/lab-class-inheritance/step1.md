# Class Inheritance

Define a class `Person` and its two child classes: `Male` and `Female`. All classes have a method `getGender` which can print `"Male"` for `Male` class and `"Female"` for `Female` class.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/class_inheritance.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class Person(object):
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


aMale = Male()
aFemale = Female()
print(aMale.getGender())
print(aFemale.getGender())

```

This Python code defines a `Person` class and two subclasses, `Male` and `Female`. The `Person` class has a `getGender` method that returns the string `"Unknown"` The `Male` and `Female` classes both inherit from the `Person` class and override the `getGender` method to return the strings `"Male"` and `"Female"`, respectively.

At the end of the code, an instance of `Male` named `aMale` and an instance of `Female` named `aFemale` are created. Their `getGender` methods are called and the results are printed to the console. Since `aMale` is an instance of the `Male` class, calling its `getGender` method returns `"Male"`, while calling the `getGender` method of `aFemale`, an instance of the `Female` class, returns `"Female"`.

Overall, this code demonstrates how to use inheritance and polymorphism to implement a simple class hierarchy and how to create objects and call their methods.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/class_inheritance.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
Male
Female
```

At this point, your code is running successfully!
