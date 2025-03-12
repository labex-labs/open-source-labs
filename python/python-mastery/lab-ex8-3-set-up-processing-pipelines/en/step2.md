# Creating Coroutine Pipeline Components

In this step, we'll create more specialized coroutines that process stock data. Each coroutine will perform a specific task in our processing pipeline.

1. Create a new file named `coticker.py` in the `/home/labex/project` directory.

2. First, add the following code to import necessary modules and define the basic structure:

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

3. You'll notice errors about `String()`, `Float()`, and `Integer()`. Let's fix those by adding the required imports at the top of the file:

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

4. Now, add the coroutine components that will form our pipeline:

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

5. Let's understand each coroutine:

   - `to_csv`: Converts raw text lines into parsed CSV rows
   - `create_ticker`: Creates Ticker objects from CSV rows
   - `negchange`: Filters for stocks with negative price changes
   - `ticker`: Formats and displays the ticker data

6. Finally, add the main program code that connects these components together:

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

7. Save the file and run it from the terminal:

```bash
cd /home/labex/project
python3 coticker.py
```

8. You should see a formatted table showing stocks with negative price changes. The output will look like:

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

The actual values may vary depending on the generated stock data.

## Understanding the Pipeline Flow

The key aspect of this program is how data flows through the coroutines:

1. The `follow` function reads lines from the `stocklog.csv` file
2. Each line is sent to `csv_parser` which parses it into CSV fields
3. The CSV data is sent to `tick_creator` which creates Ticker objects
4. The Ticker objects are sent to `neg_filter` which only passes those with negative changes
5. Finally, the filtered Ticker objects are sent to the `ticker` coroutine which formats and displays them

This pipeline architecture allows each component to focus on a single task, making the code more modular and easier to maintain.
