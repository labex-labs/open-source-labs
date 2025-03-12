# Understanding Bound Methods in Python

Methods in Python are attributes that are callable. When you access a method through an object, you get what's called a "bound method" - a method that is bound to the specific object.

## Accessing Methods as Attributes

Let's explore bound methods using our `Stock` class:

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

## Using getattr() with Methods

You can also use `getattr()` to access methods:

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

## The Bound Method and Its Object

A bound method maintains a reference to the object it was accessed from. This means that even if you store the method in a variable, it still "knows" which object it belongs to:

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

## Exploring the Bound Method Internals

A bound method has two important attributes:

- `__self__`: The object the method is bound to
- `__func__`: The actual function object

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

## Example with a Method that Takes Arguments

Let's try this with a method that takes arguments, like the `sell()` method:

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

Understanding bound methods helps you comprehend how Python's object system works under the hood, which can be useful for debugging, metaprogramming, and creating advanced programming patterns.
