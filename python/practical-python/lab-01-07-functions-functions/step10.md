# Exercise 1.33: Reading from the command line

In the `pcost.py` program, the name of the input file has been hardwired into the code:

```python
# pcost.py

def portfolio_cost(filename):
    ...
    # Your code here
    ...

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost)
```

That's fine for learning and testing, but in a real program you probably wouldn't do that.

Instead, you might pass the name of the file in as an argument to a script. Try changing the bottom part of the program as follows:

```python
# pcost.py
import sys

def portfolio_cost(filename):
    ...
    # Your code here
    ...

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
```

`sys.argv` is a list that contains passed arguments on the command line (if any).

To run your program, you'll need to run Python from the terminal.

For example, from bash on Unix:

```bash
$ python3 pcost.py portfolio.csv
Total cost: 44671.15
bash %
```
