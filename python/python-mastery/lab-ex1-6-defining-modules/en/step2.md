# Understanding the Main Module in Python

In Python, when you run a script directly, it acts as the "main" module. Python has a special variable named `__name__`. When a file is executed directly, Python sets the value of `__name__` to `"__main__"`. This is different from when the file is imported as a module.

This feature is very useful because it allows you to write code that behaves differently depending on whether the file is run directly or imported. For example, you might want some code to run only when you execute the file as a script, but not when it's imported by another script.

## Modifying pcost.py to Use the Main Module Pattern

Let's modify the `pcost.py` program to take advantage of this pattern.

1. First, you need to open the `pcost.py` file in the editor. You can use the following commands to navigate to the project directory and create the file if it doesn't exist:

```bash
cd ~/project
touch pcost.py
```

The `cd` command changes the current directory to the `project` directory in your home directory. The `touch` command creates a new file named `pcost.py` if it doesn't already exist.

2. Now, modify the `pcost.py` file to look like this:

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")

    return total_cost

# This code only runs when the file is executed as a script
if __name__ == "__main__":
    total = portfolio_cost('portfolio.dat')
    print(total)
```

The main change here is that we've wrapped the code at the end in an `if __name__ == "__main__":` condition. This means that the code inside this block will only run when the file is executed directly as a script, not when it's imported as a module.

3. After making these changes, save the file and exit the editor.

## Testing the Modified Module

Now, let's test our modified module in two different ways to see how it behaves.

1. First, run the program directly as a script using the following command:

```bash
python3 pcost.py
```

You should see the output `44671.15`, just like before. This is because when you run the script directly, the `__name__` variable is set to `"__main__"`, so the code inside the `if __name__ == "__main__":` block gets executed.

2. Next, start the Python interpreter again and import the module:

```bash
python3
```

```python
import pcost
```

This time, you won't see any output. When you import the module, the `__name__` variable is set to `"pcost"` (the module name), not `"__main__"`. So, the code inside the `if __name__ == "__main__":` block doesn't run.

3. To verify that the `portfolio_cost` function still works, you can call it like this:

```python
pcost.portfolio_cost('portfolio.dat')
```

The function should return `44671.15`, which means it's working correctly.

4. Finally, exit the Python interpreter using the following command:

```python
exit()
```

This pattern is very useful when creating Python files that can be used both as importable modules and as standalone scripts. The code inside the `if __name__ == "__main__":` block only runs when the file is executed directly, not when it's imported as a module.
