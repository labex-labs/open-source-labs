# Creating a Generator for Streaming Data

Let's apply what we've learned about generators to a real-world problem: monitoring a streaming data source. We'll create a generator that watches a log file and yields new lines as they're added.

## Setting Up the Data Source

First, let's run a simulation program that generates stock market data:

1. Open a new terminal in the WebIDE

2. Run the stock simulation program:

```bash
cd ~/project
python3 stocksim.py
```

This program will generate stock market data and write it to a file called `stocklog.csv` in the current directory. Let it run in the background while we work on the monitoring code.

## Creating a Simple File Monitor

Now, let's create a program that monitors the `stocklog.csv` file and displays any price changes that are negative:

1. Create a new file called `follow.py` in the WebIDE:

```bash
cd ~/project
```

2. Add the following code to `follow.py`:

```python
# follow.py
import os
import time

f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

3. Save the file and run it:

```bash
python3 follow.py
```

You should see output showing stocks with negative price changes, something like:

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

Press `Ctrl+C` to stop the program.

## Converting to a Generator Function

Now, let's refactor our code to use a generator function. This will make the code more reusable and modular:

1. Open `follow.py` again and modify it:

```python
# follow.py
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file as they are added.
    Similar to the 'tail -f' Unix command.
    """
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move to the end of the file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example usage - monitor stocks with negative price changes
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

2. Save the file and run it again:

```bash
python3 follow.py
```

The output should be the same as before, but now the file monitoring logic is neatly encapsulated in a generator function that can be reused in other contexts.

## Understanding the Power of Generators

Notice how we've taken a pattern of reading from a file and turned it into a reusable generator function. The `follow()` function can now be used in any program that needs to monitor a file, not just for stock data.

For example, you could use it to monitor server logs, application logs, or any other file that gets updated over time. This demonstrates the power of generators for handling streaming data sources in a clean, modular way.
