# Subclass of Class

Define a class named `American` and its subclass `NewYorker`.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/subclass_of_class.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class American():
    pass


class NewYorker(American):
    pass


american = American()
newyorker = NewYorker()

print(american)
print(newyorker)

```

This Python code defines two classes called `American` and `NewYorker`. The `NewYorker` class is a subclass of the `American` class, which means that it inherits all the attributes and methods of the `American` class.

The code then creates an instance of the `American` class called `american` and an instance of the `NewYorker` class called `newyorker`.

Finally, the code uses the `print()` function to output the memory addresses of the `american` and `newyorker` instances to the console.

Overall, this code demonstrates how to define and use classes and instances in Python. It also shows how inheritance works in Python, where a subclass can inherit attributes and methods from its superclass.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/subclass_of_class.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program may be:

```bash
<__main__.American object at 0x0000022E6E4123A0>
<__main__.NewYorker object at 0x0000022E6E4123D0>
```

At this point, your code is running successfully!
