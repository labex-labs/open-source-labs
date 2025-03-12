# Creating the Ticker Class

In data processing, working with raw data can be quite challenging. To make our work with stock data more organized and efficient, we'll define a proper class to represent stock quotes. This class will serve as a blueprint for our stock data, making our data processing pipeline more robust and easier to manage.

## Creating the ticker.py File

1. First, we need to create a new file in the WebIDE. You can do this by clicking on the "New File" icon or right - clicking in the file explorer and selecting "New File". Name this file `ticker.py`. This file will hold the code for our `Ticker` class.

2. Now, let's add the following code to your newly created `ticker.py` file. This code will define our `Ticker` class and set up a simple processing pipeline to test it.

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

3. After adding the code, save the file. You can do this by pressing `Ctrl+S` or selecting "File" → "Save" from the menu. Saving the file ensures that your changes are preserved and can be run later.

## Understanding the Code

Let's take a closer look at what this code does step by step:

1. At the beginning of the code, we're importing `Structure` and field types from the `structure.py` module. This module has already been set up for you. These imports are essential because they provide the building blocks for our `Ticker` class. The `Structure` class will be the base class for our `Ticker` class, and the field types like `String`, `Float`, and `Integer` will define the data types of our stock data fields.

2. Next, we define a `Ticker` class that inherits from `Structure`. This class has several fields that represent different aspects of the stock data:

   - `name`: This field stores the stock symbol, such as "IBM" or "AAPL". It helps us identify which company's stock we're dealing with.
   - `price`: It holds the current price of the stock. This is a crucial piece of information for investors.
   - `date` and `time`: These fields tell us when the stock quote was generated. Knowing the time and date is important for analyzing stock price trends over time.
   - `change`: This represents the price change of the stock. It shows whether the stock price has gone up or down compared to a previous point.
   - `open`, `high`, `low`: These fields represent the opening price, the highest price, and the lowest price of the stock during a certain period. They give us an idea of the stock's price range.
   - `volume`: This field stores the number of shares traded. High trading volume can indicate strong market interest in a particular stock.

3. In the `if __name__ == '__main__':` block, we set up a processing pipeline. This block of code will be executed when we run the `ticker.py` file directly.
   - `follow('stocklog.csv')` is a function that generates lines from the `stocklog.csv` file. It allows us to read the file line by line.
   - `csv.reader(lines)` takes these lines and parses them into row data. CSV (Comma - Separated Values) is a common file format for storing tabular data, and this function helps us extract the data from each row.
   - `(Ticker.from_row(row) for row in rows)` is a generator expression. It takes each row of data and converts it into a `Ticker` object. This way, we transform the raw CSV data into structured objects that are easier to work with.
   - The `for` loop iterates over these `Ticker` objects and prints each one. This allows us to see the structured data in action.

## Running the Code

Let's run the code to see how it works:

1. First, we need to make sure we're in the project directory in the terminal. If you're not already there, use the following command to navigate to it:

   ```bash
   cd /home/labex/project
   ```

2. Once you're in the correct directory, run the `ticker.py` script using the following command:

   ```bash
   python3 ticker.py
   ```

3. After running the script, you should see output similar to this (your data will vary):
   ```
   Ticker(IBM, 103.53, 6/11/2007, 09:53.59, 0.46, 102.87, 103.53, 102.77, 541633)
   Ticker(MSFT, 30.21, 6/11/2007, 09:54.01, 0.16, 30.05, 30.21, 29.95, 7562516)
   Ticker(AA, 40.01, 6/11/2007, 09:54.01, 0.35, 39.67, 40.15, 39.31, 576619)
   Ticker(T, 40.1, 6/11/2007, 09:54.08, -0.16, 40.2, 40.19, 39.87, 1312959)
   ```

You can stop the execution of the script by pressing `Ctrl+C` when you've seen enough output.

Notice how the raw CSV data has been transformed into structured `Ticker` objects. This transformation makes the data much easier to work with in our processing pipeline, as we can now access and manipulate the stock data using the fields defined in the `Ticker` class.
