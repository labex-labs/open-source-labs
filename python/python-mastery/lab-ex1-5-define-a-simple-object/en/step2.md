# Creating the Stock Class

In Python, a class is a blueprint for creating objects. It allows you to bundle data and functionality together. Now, let's create our `Stock` class to represent stock information. A stock has certain characteristics, such as its name, the number of shares, and the price per share. We will define attributes for these aspects within our class.

1. First, you need to be in the correct directory in the WebIDE. If you're not already in the `/home/labex/project` directory, navigate to it. This is where we'll be working on our `Stock` class code.

2. Once you're in the right directory, create a new file in the editor. Name this file `stock.py`. This file will hold the code for our `Stock` class.

3. Now, let's add the code to define the `Stock` class. Copy and paste the following code into the `stock.py` file:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

In this code:

- The `class Stock:` statement creates a new class named `Stock`. This is like a template for creating stock objects.
- The `__init__` method is a special method in Python classes. It is called a constructor. When you create a new object of the `Stock` class, the `__init__` method will run automatically. It takes three parameters: `name`, `shares`, and `price`. These parameters represent the information about the stock.
- Inside the `__init__` method, we use `self` to refer to the instance of the class. We store the values of the parameters as instance attributes. For example, `self.name = name` stores the `name` parameter as an attribute of the object.
- The `cost()` method is a custom method we defined. It calculates the total cost of the stock by multiplying the number of shares (`self.shares`) by the price per share (`self.price`).

4. After adding the code, save the file. You can do this by pressing `Ctrl+S` or clicking the Save icon. Saving the file ensures that your changes are preserved.

Let's examine the code again to make sure we understand it:

- We defined a class named `Stock`. This class will be used to create stock objects.
- The `__init__` method takes three parameters: `name`, `shares`, and `price`. It initializes the object's attributes with these values.
- Inside `__init__`, we store these parameters as instance attributes using `self`. This allows each object to have its own set of values for these attributes.
- We added a `cost()` method that calculates the total cost by multiplying shares by price. This is a useful functionality for our stock objects.

When we create a `Stock` object, the `__init__` method will run automatically, setting up the initial state of our object with the values we provide. This way, we can easily create multiple stock objects with different names, numbers of shares, and prices.
