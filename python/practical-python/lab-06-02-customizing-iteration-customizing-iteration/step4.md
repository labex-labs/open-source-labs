# Exercise 6.5: Monitoring a streaming data source

Generators can be an interesting way to monitor real-time data sources such as log files or stock market feeds. In this part, we'll explore this idea. To start, follow the next instructions carefully.

The program `Data/stocksim.py` is a program that simulates stock market data. As output, the program constantly writes real-time data to a file `Data/stocklog.csv`. In a separate command window go into the `Data/` directory and run this program:

```bash
$ python3 stocksim.py
```

If you are on Windows, just locate the `stocksim.py` program and double-click on it to run it. Now, forget about this program (just let it run). Using another window, look at the file `Data/stocklog.csv` being written by the simulator. You should see new lines of text being added to the file every few seconds. Again, just let this program run in the background---it will run for several hours (you shouldn't need to worry about it).

Once the above program is running, let's write a little program to open the file, seek to the end, and watch for new output. Create a file `follow.py` and put this code in it:

```python
# follow.py
import os
import time

f = open('Data/stocklog.csv')
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
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

If you run the program, you'll see a real-time stock ticker. Under the hood, this code is kind of like the Unix `tail -f` command that's used to watch a log file.

Note: The use of the `readline()` method in this example is somewhat unusual in that it is not the usual way of reading lines from a file (normally you would just use a `for`-loop). However, in this case, we are using it to repeatedly probe the end of the file to see if more data has been added (`readline()` will either return new data or an empty string).
