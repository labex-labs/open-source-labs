# Implementing an Abstract Base Class

In this step, you will convert the `TableFormatter` class into a proper abstract base class (ABC) using Python's `abc` module. This ensures that subclasses implement all required methods.

## Understanding Abstract Base Classes

An abstract base class is a class that cannot be instantiated and requires specific methods to be implemented by its subclasses. This is useful for defining interfaces in Python.

Key concepts:

- ABCs are created using the `abc` module
- Methods marked with `@abstractmethod` must be implemented by subclasses
- Attempting to instantiate a class that inherits from an ABC without implementing all required methods will raise an error

## Modifying the TableFormatter Class

Open the `tableformat.py` file and modify the `TableFormatter` class to use the `abc` module:

1. First, add the required import at the top of the file:

```python
# tableformat.py
from abc import ABC, abstractmethod
```

2. Then, modify the `TableFormatter` class to inherit from `ABC` and mark its methods as abstract:

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

Notice that:

- The class now inherits from `ABC`
- Both methods are decorated with `@abstractmethod`
- The `NotImplementedError` has been replaced with `pass` since the `@abstractmethod` decorator handles the enforcement

## Testing Your Abstract Base Class

Let's test if your abstract base class works correctly. Create a file called `test_abc.py` with the following code:

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

Run the test file:

```bash
python test_abc.py
```

You should see output similar to:

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

This confirms that your abstract base class is correctly enforcing the implementation of required methods. The first test case fails because it has a method named `headers` instead of `headings`, while the second test case passes because it properly implements all required methods.
