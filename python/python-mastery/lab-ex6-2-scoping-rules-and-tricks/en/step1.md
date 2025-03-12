# Understanding the Problem with Class Initialization

In the programming world, classes are a fundamental concept that allows you to create custom data types. In previous exercises, you might have created a `Structure` class. This class serves as a useful tool for easily defining data structures. A data structure is a way to organize and store data so that it can be accessed and used efficiently. The `Structure` class, as a base class, takes care of initializing attributes based on a predefined list of field names. Attributes are variables that belong to an object, and field names are the names we give to these attributes.

Let's take a closer look at the current implementation of the `Structure` class. To do this, we need to open the `structure.py` file in the code editor. This file contains the code for the `Structure` class. Here are the commands to navigate to the project directory and open the file:

```bash
cd ~/project
code structure.py
```

The `Structure` class provides a basic framework for defining simple data structures. When we create a subclass, like the `Stock` class, we can define the specific fields we want for that subclass. A subclass inherits the properties and methods of its base class, in this case, the `Structure` class. For example, in the `Stock` class, we define the fields `name`, `shares`, and `price`:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')
```

Now, let's open the `stock.py` file to see how the `Stock` class is implemented in the context of the overall code. This file likely contains the code that uses the `Stock` class and interacts with it. Use the following command to open the file:

```bash
code stock.py
```

Although this approach of using the `Structure` class and its subclasses works, it has several limitations. To identify these issues, we'll run the Python interpreter and explore how the `Stock` class behaves. The following command will import the `Stock` class and display its help information:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

When you run this command, you'll notice that the signature shown in the help output isn't very helpful. Instead of showing the actual parameter names like `name`, `shares`, and `price`, it only shows `*args`. This lack of clear parameter names makes it difficult for users to understand how to correctly create an instance of the `Stock` class.

Let's also try to create a `Stock` instance using keyword arguments. Keyword arguments allow you to specify the values for parameters by their names, which can make the code more readable. Run the following command:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

You should get an error message like this:

```
TypeError: __init__() got an unexpected keyword argument 'name'
```

This error occurs because our current `__init__` method, which is responsible for initializing objects of the `Stock` class, doesn't handle keyword arguments. It only accepts positional arguments, which means you have to provide the values in a specific order without using the parameter names. This is a limitation that we want to fix in this lab.

In this lab, we'll explore different approaches to make our `Structure` class more flexible and user-friendly. By doing so, we can improve the usability of the `Stock` class and other subclasses of `Structure`.
