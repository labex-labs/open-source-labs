# Implementing an Abstract Base Class

In this step, we're going to convert the `TableFormatter` class into a proper abstract base class (ABC) using Python's `abc` module. But first, let's understand what an abstract base class is and why we need it.

## Understanding Abstract Base Classes

An abstract base class is a special type of class in Python. It's a class that you can't create an object from directly, which means you can't instantiate it. The main purpose of an abstract base class is to define a common interface for its subclasses. It sets a set of rules that all subclasses must follow. Specifically, it requires subclasses to implement certain methods.

Here are some key concepts about abstract base classes:

- We use the `abc` module in Python to create abstract base classes.
- Methods marked with the `@abstractmethod` decorator are like rules. Any subclass that inherits from an abstract base class must implement these methods.
- If you try to create an object of a class that inherits from an abstract base class but hasn't implemented all the required methods, Python will raise an error.

Now that you understand the basics of abstract base classes, let's see how we can modify the `TableFormatter` class to become one.

## Modifying the TableFormatter Class

Open the `tableformat.py` file. We're going to make some changes to the `TableFormatter` class so that it uses the `abc` module and becomes an abstract base class.

1. First, we need to import the necessary things from the `abc` module. Add the following import statement at the top of the file:

```python
# tableformat.py
from abc import ABC, abstractmethod
```

This import statement brings in two important things: `ABC`, which is a base class for all abstract base classes in Python, and `abstractmethod`, which is a decorator we'll use to mark methods as abstract.

2. Next, we'll modify the `TableFormatter` class. It should inherit from `ABC` to become an abstract base class, and we'll mark its methods as abstract using the `@abstractmethod` decorator. Here's how the modified class should look:

```python
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        pass
```

Notice a few things about this modified class:

- The class now inherits from `ABC`, which means it's officially an abstract base class.
- Both the `headings` and `row` methods are decorated with `@abstractmethod`. This tells Python that any subclass of `TableFormatter` must implement these methods.
- We replaced the `NotImplementedError` with `pass`. The `@abstractmethod` decorator takes care of making sure subclasses implement these methods, so we don't need the `NotImplementedError` anymore.

## Testing Your Abstract Base Class

Now that we've made the `TableFormatter` class an abstract base class, let's test if it works correctly. We'll create a file called `test_abc.py` with the following code:

```python
from tableformat import TableFormatter

# Test case 1: Define a class with a misspelled method
try:
    class NewFormatter(TableFormatter):
        def headers(self, headings):  # Misspelled 'headings'
            pass
        def row(self, rowdata):
            pass

    f = NewFormatter()
    print("Test 1 failed - abstract method enforcement not working")
except TypeError as e:
    print(f"Test 1 passed - caught error: {e}")

# Test case 2: Define a class that properly implements all methods
try:
    class ProperFormatter(TableFormatter):
        def headings(self, headers):
            pass
        def row(self, rowdata):
            pass

    f = ProperFormatter()
    print("Test 2 passed - proper implementation works")
except TypeError as e:
    print(f"Test 2 failed - error: {e}")
```

In this code, we have two test cases. The first test case defines a class `NewFormatter` that tries to inherit from `TableFormatter` but has a misspelled method name. The second test case defines a class `ProperFormatter` that correctly implements all the required methods.

To run the test, open your terminal and run the following command:

```bash
python test_abc.py
```

You should see output similar to this:

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

This output confirms that our abstract base class is working as expected. The first test case fails because the `NewFormatter` class didn't implement the `headings` method correctly. The second test case passes because the `ProperFormatter` class implemented all the required methods.
