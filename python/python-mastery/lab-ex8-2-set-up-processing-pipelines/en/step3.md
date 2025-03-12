# Building a More Complex Data Pipeline

Now let's enhance our data pipeline by adding filtering and better presentation. We'll modify our `ticker.py` script to filter the data and display it in a nicely formatted table.

## Updating the ticker.py File

1. Open your `ticker.py` file in the WebIDE.

2. Replace the `if __name__ == '__main__':` block with the following code:

```python
if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name', 'price', 'change'], formatter)
```

3. Save the file by pressing `Ctrl+S` or selecting "File" → "Save" from the menu.

## Understanding the Enhanced Pipeline

Let's break down what this enhanced pipeline does:

1. We import `create_formatter` and `print_table` from the `tableformat` module, which is already set up for you.

2. We create a text formatter with `create_formatter('text')`.

3. We set up our pipeline:
   - `follow('stocklog.csv')` generates lines from the file
   - `csv.reader(lines)` parses these lines into row data
   - `(Ticker.from_row(row) for row in rows)` converts each row into a `Ticker` object
   - `(rec for rec in records if rec.change < 0)` filters to only show stocks with negative price changes
   - `print_table(negative, ['name', 'price', 'change'], formatter)` formats and prints the filtered data

This pipeline showcases the power of generators: we're chaining together multiple operations (reading, parsing, converting, filtering) without storing all the data in memory at once.

## Running the Enhanced Pipeline

Let's run the updated code:

1. In the terminal, navigate to your project directory if you're not already there:

   ```bash
   cd /home/labex/project
   ```

2. Run the `ticker.py` script:

   ```bash
   python3 ticker.py
   ```

3. You should see a nicely formatted table showing only stocks with negative price changes:
   ```
          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19
   ```

You can stop the execution by pressing `Ctrl+C` when you've seen enough output.

## The Power of Generator Pipelines

What we've created is a powerful data processing pipeline that:

1. Continuously monitors a file for new data
2. Parses the CSV data into structured objects
3. Filters the data based on specific criteria (negative price changes)
4. Formats and presents the data in a readable table

All of this is done with minimal memory usage because generators produce values on-demand rather than storing everything in memory. This approach is similar to Unix pipes, where each component processes data and passes it to the next component.

You can think of generators as Lego blocks that you can stack together to create powerful data processing workflows. This modular approach allows you to build complex systems from simple, reusable components.
