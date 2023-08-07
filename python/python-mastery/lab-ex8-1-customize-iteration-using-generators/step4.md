# Monitoring a streaming data source

Generators can also be a useful way to simply produce a stream of data. In this part, we'll explore this idea by writing a generator to watch a log file. To start, follow the next instructions carefully.

The program `stocksim.py` is a program that simulates stock market data. As output, the program constantly writes real-time data to a file `stocklog.csv`. In a command window (not IDLE) go into the \`\` directory and run this program:

    % python3 stocksim.py

If you are on Windows, just locate the `stocksim.py` program and double-click on it to run it. Now, forget about this program (just let it run). Again, just let this program run in the background---it will run for several hours (you shouldn't need to worry about it).

Once the above program is running, let's write a little program to open the file, seek to the end, and watch for new output. Create a file `follow.py` and put this code in it:

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

If you run the program, you'll see a real-time stock ticker. Under the covers, this code is kind of like the Unix `tail -f` command that's used to watch a log file.

**Note:** The use of the `readline()` method in this example is somewhat unusual in that it is not the usual way of reading lines from a file (normally you would just use a `for`-loop). However, in this case, we are using it to repeatedly probe the end of the file to see if more data has been added (`readline()` will either return new data or an empty string).

If you look at the code carefully, the first part of the code is producing lines of data whereas the statements at the end of the `while` loop are consuming the data. A major feature of generator functions is that you can move all of the data production code into a reusable function.

Modify the code so that the file-reading is performed by a generator function `follow(filename)`. Make it so the following code works:

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Should see lines of output produced here ...
```

Modify the stock ticker code so that it looks like this:

```python
for line in follow('stocklog.csv'):
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

**Discussion**

Something very powerful just happened here. You moved an interesting iteration pattern (reading lines at the end of a file) into its own little function. The `follow()` function is now this completely general purpose utility that you can use in any program. For example, you could use it to watch server logs, debugging logs, and other similar data sources. That's kind of cool.
