# Creating a Generator for Streaming Data

In programming, generators are a powerful tool, especially when dealing with real - world problems like monitoring a streaming data source. In this section, we'll learn how to apply what we've learned about generators to such a practical scenario. We're going to create a generator that keeps an eye on a log file and gives us new lines as they're added to the file.

## Setting Up the Data Source

Before we start creating the generator, we need to set up a data source. In this case, we'll use a simulation program that generates stock market data.

First, you need to open a new terminal in the WebIDE. This is where you'll run commands to start the simulation.

After opening the terminal, you'll run the stock simulation program. Here are the commands you need to enter:

```bash
cd ~/project
python3 stocksim.py
```

The first command `cd ~/project` changes the current directory to the `project` directory in your home directory. The second command `python3 stocksim.py` runs the stock simulation program. This program will generate stock market data and write it to a file named `stocklog.csv` in the current directory. Let this program run in the background while we work on the monitoring code.

## Creating a Simple File Monitor

Now that we have our data source set up, let's create a program that monitors the `stocklog.csv` file. This program will display any price changes that are negative.

1. First, create a new file called `follow.py` in the WebIDE. To do this, you need to change the directory to the `project` directory using the following command in the terminal:

```bash
cd ~/project
```

2. Next, add the following code to the `follow.py` file. This code opens the `stocklog.csv` file, moves the file pointer to the end of the file, and then continuously checks for new lines. If a new line is found and it represents a negative price change, it prints the stock name, price, and change.

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

3. After adding the code, save the file. Then, run the program using the following command in the terminal:

```bash
python3 follow.py
```

You should see output that shows stocks with negative price changes. It might look something like this:

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

If you want to stop the program, press `Ctrl+C` in the terminal.

## Converting to a Generator Function

While the previous code works, we can make it more reusable and modular by converting it to a generator function. A generator function is a special type of function that can be paused and resumed, and it yields values one at a time.

1. Open the `follow.py` file again and modify it to use a generator function. Here's the updated code:

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

The `follow` function is now a generator function. It opens the file, moves to the end, and then continuously checks for new lines. When a new line is found, it yields that line.

2. Save the file and run it again using the command:

```bash
python3 follow.py
```

The output should be the same as before. But now, the file monitoring logic is neatly encapsulated in the `follow` generator function. This means we can reuse this function in other programs that need to monitor a file.

## Understanding the Power of Generators

By converting our file - reading code into a generator function, we've made it much more flexible and reusable. The `follow()` function can be used in any program that needs to monitor a file, not just for stock data.

For example, you could use it to monitor server logs, application logs, or any other file that gets updated over time. This shows how generators are a great way to handle streaming data sources in a clean and modular way.
