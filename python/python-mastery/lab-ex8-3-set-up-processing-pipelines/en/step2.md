# Creating Coroutine Pipeline Components

In this step, we're going to create more specialized coroutines for processing stock data. A coroutine is a special type of function that can pause and resume its execution, which is very useful for building data processing pipelines. Each coroutine we create will perform a specific task in our overall processing pipeline.

1. First, you need to create a new file. Navigate to the `/home/labex/project` directory and create a file named `coticker.py`. This file will hold all the code for our coroutine - based data processing.

2. Now, let's start writing code in the `coticker.py` file. We'll first import the necessary modules and define the basic structure. Modules are pre - written code libraries that provide useful functions and classes. The following code does just that:

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

3. When you look at the code above, you'll notice that there are errors related to `String()`, `Float()`, and `Integer()`. These are classes that we need to import. So, we'll add the required imports at the top of the file. This way, Python knows where to find these classes. Here's the updated code:

```python
# coticker.py
from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

4. Next, we'll add the coroutine components that will form our data processing pipeline. Each coroutine has a specific job in the pipeline. Here's the code to add these coroutines:

```python
@consumer
def to_csv(target):
    def producer():
        while True:
            line = yield

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

5. Let's understand what each of these coroutines does:
   - `to_csv`: Its job is to convert raw text lines into parsed CSV rows. This is important because our data is initially in text format, and we need to break it into structured CSV data.
   - `create_ticker`: This coroutine takes the CSV rows and creates `Ticker` objects from them. `Ticker` objects represent the stock data in a more organized way.
   - `negchange`: It filters the `Ticker` objects. It only passes on the stocks that have negative price changes. This helps us focus on the stocks that are losing value.
   - `ticker`: This coroutine formats and displays the ticker data. It uses a formatter to present the data in a nice, readable table.

6. Finally, we need to add the main program code that connects all these components together. This code will set up the data flow through the pipeline. Here's the code:

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change']

    # Create the processing pipeline
    t = ticker('text', fields)
    neg_filter = negchange(t)
    tick_creator = create_ticker(neg_filter)
    csv_parser = to_csv(tick_creator)

    # Connect the pipeline to the data source
    follow('stocklog.csv', csv_parser)
```

7. After writing all the code, save the `coticker.py` file. Then, open the terminal and run the following commands. The `cd` command changes the directory to where our file is located, and the `python3` command runs our Python script:

```bash
cd /home/labex/project
python3 coticker.py
```

8. If everything goes well, you should see a formatted table in the terminal. This table shows stocks with negative price changes. The output will look something like this:

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

Keep in mind that the actual values in the table may vary depending on the generated stock data.

## Understanding the Pipeline Flow

The most important part of this program is how data flows through the coroutines. Let's break it down step by step:

1. The `follow` function starts by reading lines from the `stocklog.csv` file. This is our data source.
2. Each line that is read is then sent to the `csv_parser` coroutine. The `csv_parser` takes the raw text line and parses it into CSV fields.
3. The parsed CSV data is then sent to the `tick_creator` coroutine. This coroutine creates `Ticker` objects from the CSV rows.
4. The `Ticker` objects are then sent to the `neg_filter` coroutine. This coroutine checks each `Ticker` object. If the stock has a negative price change, it passes the object on; otherwise, it discards it.
5. Finally, the filtered `Ticker` objects are sent to the `ticker` coroutine. The `ticker` coroutine formats the data and displays it in a table.

This pipeline architecture is very useful because it allows each component to focus on a single task. This makes the code more modular, which means it's easier to understand, modify, and maintain.
