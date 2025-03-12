# Returning Multiple Values from Functions

In Python, when you need a function to return more than one value, there's a handy solution: returning a tuple. A tuple is a type of data structure in Python. It's an immutable sequence, which means once you create a tuple, you can't change its elements. Tuples are useful because they can hold multiple values of different types all in one place.

Let's create a function to parse configuration lines in the format `name=value`. The goal of this function is to take a line in this format and return both the name and the value as separate items.

1. First, you need to create a new Python file. This file will hold the code for our function and the test code. In the project directory, create a file named `return_values.py`. You can use the following command in the terminal to create this file:

```
touch ~/project/return_values.py
```

2. Now, open the `return_values.py` file in your code editor. Inside this file, we'll write the `parse_line` function. This function takes a line as input, splits it at the first '=' sign, and returns the name and value as a tuple.

```python
def parse_line(line):
    """
    Parse a line in the format 'name=value' and return both the name and value.

    Args:
        line (str): Input line to parse in the format 'name=value'

    Returns:
        tuple: A tuple containing (name, value)
    """
    parts = line.split('=', 1)  # Split at the first equals sign
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Return as a tuple
```

In this function, the `split` method is used to divide the input line into two parts at the first '=' sign. If the line is in the correct `name=value` format, we extract the name and value and return them as a tuple.

3. After defining the function, we need to add some test code to see if the function works as expected. The test code will call the `parse_line` function with a sample input and print the results.

```python
# Test the parse_line function
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # Unpacking the tuple into separate variables
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

In the test code, we first call the `parse_line` function and store the returned tuple in the `result` variable. Then we print this tuple. Next, we use tuple unpacking to directly assign the elements of the tuple to the `name` and `value` variables and print them separately.

4. Once you've written the function and the test code, save the `return_values.py` file. Then, open the terminal and run the following command to execute the Python script:

```
python ~/project/return_values.py
```

You should see output similar to:

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**Explanation:**

- The `parse_line` function splits the input string at the '=' character using the `split` method. This method divides the string into parts based on the specified separator.
- It returns both parts as a tuple using the syntax `return (name, value)`. A tuple is a way to group multiple values together.
- When calling the function, you have two options. You can either store the entire tuple in one variable, like we did with the `result` variable. Or you can "unpack" the tuple directly into separate variables using the syntax `name, value = parse_line(...)`. This makes it easier to work with the individual values.

This pattern of returning multiple values as a tuple is very common in Python. It makes functions more versatile because they can provide more than one piece of information to the code that calls them.
