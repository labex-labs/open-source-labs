# Understanding Bound Methods in Python

In Python, methods are a special type of attributes that you can call. When you access a method through an object, you're getting what we call a "bound method". A bound method is essentially a method that's tied to a specific object. This means it has access to the object's data and can operate on it.

## Accessing Methods as Attributes

Let's start exploring bound methods using our `Stock` class. First, we'll see how to access a method as an attribute of an object.

```python
# Open a Python interactive shell
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Access the cost method without calling it
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# You can also do this in one step
print(s.cost())  # Output: 49010.0
```

In the code above, we first import the `Stock` class and create an instance of it. Then we access the `cost` method of the `s` object without actually calling it. This gives us a bound method. When we call this bound method, it calculates the cost based on the object's data. You can also directly call the method on the object in one step.

## Using getattr() with Methods

Another way to access methods is by using the `getattr()` function. This function allows you to get an attribute of an object by its name.

```python
# Get the cost method using getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# Get and call in one step
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

Here, we use `getattr()` to get the `cost` method from the `s` object. Just like before, we can call the bound method to get the result. And you can even get and call the method in a single line.

## The Bound Method and Its Object

A bound method always keeps a reference to the object it was accessed from. This means that even if you store the method in a variable, it still knows which object it belongs to and can access the object's data.

```python
# Store the cost method in a variable
c = s.cost

# Call the method
print(c())  # Output: 49010.0

# Change the object's state
s.shares = 75

# Call the method again - it sees the updated state
print(c())  # Output: 36757.5
```

In this example, we store the `cost` method in a variable `c`. When we call `c()`, it calculates the cost based on the object's current data. Then we change the `shares` attribute of the `s` object. When we call `c()` again, it uses the updated data to calculate the new cost.

## Exploring the Bound Method Internals

A bound method has two important attributes that give us more information about it.

- `__self__`: This attribute refers to the object the method is bound to.
- `__func__`: This attribute is the actual function object that represents the method.

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

Here, we access the `__self__` and `__func__` attributes of the bound method `c`. We can see that `__self__` is the `s` object, and `__func__` is the `cost` function. We can even manually call the function by passing the object as an argument, and it gives us the same result as calling the bound method directly.

## Example with a Method that Takes Arguments

Let's see how bound methods work with a method that takes arguments, like the `sell()` method.

```python
# Get the sell method
sell_method = s.sell

# Examine the method
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Call the method with an argument
sell_method(25)
print(s.shares)  # Output: 50

# Call the method manually using __func__ and __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

In this example, we get the `sell` method as a bound method. When we call it with an argument, it updates the `shares` attribute of the `s` object. We can also manually call the method using the `__func__` and `__self__` attributes, passing the argument as well.

Understanding bound methods helps you comprehend how Python's object system works under the hood, which can be useful for debugging, metaprogramming, and creating advanced programming patterns.
