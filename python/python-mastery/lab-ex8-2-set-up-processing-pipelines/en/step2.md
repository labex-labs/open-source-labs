# Creating the Ticker Class

Now let's create a more structured way to work with the stock data by defining a proper class to represent stock quotes. This will make our data processing pipeline more robust and easier to use.

## Creating the ticker.py File

1. In the WebIDE, create a new file called `ticker.py` by clicking on the "New File" icon or right-clicking in the file explorer and selecting "New File".

2. Add the following code to your `ticker.py` file:

```python
# ticker.py

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

if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
```

3. Save the file by pressing `Ctrl+S` or selecting "File" → "Save" from the menu.

## Understanding the Code

Let's break down what this code does:

1. We're importing `Structure` and field types from the `structure.py` module that's already set up for you.

2. We define a `Ticker` class that inherits from `Structure`. It has fields for all the stock data:

   - `name`: The stock symbol (e.g., "IBM", "AAPL")
   - `price`: The current stock price
   - `date` and `time`: When the quote was generated
   - `change`: The price change
   - `open`, `high`, `low`: Opening price, highest price, and lowest price
   - `volume`: Number of shares traded

3. In the `if __name__ == '__main__':` block, we set up a processing pipeline:
   - `follow('stocklog.csv')` generates lines from the file
   - `csv.reader(lines)` parses these lines into row data
   - `(Ticker.from_row(row) for row in rows)` is a generator expression that converts each row into a `Ticker` object
   - The `for` loop prints each `Ticker` object

## Running the Code

Let's run the code to see it in action:

1. In the terminal, navigate to your project directory if you're not already there:

   ```bash
   cd /home/labex/project
   ```

2. Run the `ticker.py` script:

   ```bash
   python3 ticker.py
   ```

3. You should see output similar to this (your data will vary):
   ```
   Ticker(IBM, 103.53, 6/11/2007, 09:53.59, 0.46, 102.87, 103.53, 102.77, 541633)
   Ticker(MSFT, 30.21, 6/11/2007, 09:54.01, 0.16, 30.05, 30.21, 29.95, 7562516)
   Ticker(AA, 40.01, 6/11/2007, 09:54.01, 0.35, 39.67, 40.15, 39.31, 576619)
   Ticker(T, 40.1, 6/11/2007, 09:54.08, -0.16, 40.2, 40.19, 39.87, 1312959)
   ```

You can stop the execution by pressing `Ctrl+C` when you've seen enough output.

Notice how the raw CSV data has been transformed into structured `Ticker` objects. This makes the data much easier to work with in our processing pipeline.
