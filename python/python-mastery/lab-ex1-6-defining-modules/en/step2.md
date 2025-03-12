# Understanding the Main Module in Python

In Python, when you run a script directly, it executes as the "main" module. Python sets a special variable called `__name__` to `"__main__"` when a file is executed directly, rather than being imported.

This allows you to write code that behaves differently when the file is run directly versus when it's imported as a module.

## Modifying pcost.py to Use the Main Module Pattern

Let's modify the `pcost.py` program to use this pattern:

1. Open the `pcost.py` file in the editor:

```bash
cd ~/project
touch pcost.py
```

2. Modify the file to look like this:

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

The key change is wrapping the code at the end in an `if __name__ == "__main__":` condition.

3. Save and exit the editor.

## Testing the Modified Module

Now let's test our modified module in two different ways:

1. Run the program directly as a script:

```bash
python3 pcost.py
```

You should see the output `44671.15`, just like before. This is because the code inside the `if __name__ == "__main__":` block executes when the script is run directly.

2. Now, start the Python interpreter again and import the module:

```bash
python3
```

```python
import pcost
```

This time, you should not see any output. The calculation code doesn't run automatically because when imported, the `__name__` variable is set to `"pcost"` (the module name), not `"__main__"`.

3. Verify the function still works:

```python
pcost.portfolio_cost('portfolio.dat')
```

The function should return `44671.15`.

4. Exit the Python interpreter:

```python
exit()
```

This pattern is very useful when creating Python files that can serve both as importable modules and as standalone scripts. The code inside the `if __name__ == "__main__":` block only runs when the file is executed directly, not when it's imported as a module.
