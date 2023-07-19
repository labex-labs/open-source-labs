# Static Method of Class

Define a class named `American` which has a static method called `printNationality`.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/static_method_of_class.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class American():
    @staticmethod
    def printNationality():
        print("I am American")


american = American()
# this will not run if @staticmethod does not decorates the function.
american.printNationality()
# Because the class has no instance.

American.printNationality()   # this will run even though the @staticmethod
# does not decorate printNationality()

```

This Python code defines a class called `American` that contains a static method called `printNationality()`. The `printNationality()` method simply prints the message "I am American" to the console.

The code then creates an instance of the `American` class called `american`. The `printNationality()` method is called on the `american` instance using the dot notation.

Since `printNationality()` is a static method, it can be called on the class itself without the need for an instance. The code demonstrates this by calling `printNationality()` on the `American` class directly.

Overall, this code demonstrates how to define and use a static method in a Python class. Static methods are methods that belong to the class itself rather than to any instance of the class. They can be called on the class directly or on an instance of the class.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/static_method_of_class.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
I am American
I am American
```

At this point, your code is running successfully!

## Hints

- Use `@staticmethod` decorator to define class static method.There are also two more methods.To know more, go to this [link](https://realpython.com/blog/python/instance-class-and-static-methods-demystified/).
