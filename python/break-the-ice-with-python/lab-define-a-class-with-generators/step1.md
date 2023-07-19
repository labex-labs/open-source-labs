# Define a Class with Generators

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/define_a_class_with_generators.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class Divisible:

    def by_seven(self, n):
        for number in range(0, n + 1):
            if number % 7 == 0:
                yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)

```

This Python code defines a class called `Divisible`, which contains a method called `by_seven`. The method takes an integer parameter `n` and uses the `yield` statement to generate a generator object that contains all the integers between 0 and `n` that are divisible by 7.

In the main program, an instance of the `Divisible` class called `divisible` is created, and its `by_seven` method is called with the user-input integer as the argument. This returns a generator object that can be used to iterate over all the integers that are divisible by 7.

Then, a `for` loop is used to iterate over the generator object, and the `print` function is used to output each integer to the console.

Overall, this code demonstrates how to use a generator function to generate a iterable object that contains all the integers that meet a specific condition. It also shows how to use an instance of a class to call a method and use the resulting generator object to iterate over the results and output them to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/define_a_class_with_generators.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
7
```

Then, the output of the program should be:

```bash
0
7
```

At this point, your code is running successfully!
