# Basic Generator Pipeline with CSV Data

In this step, you will learn how to create a basic processing pipeline using generators. Generators are a special type of iterator in Python that generate values on-demand, which makes them memory-efficient for processing large data streams.

## Understanding Generators

A generator is a function that returns an iterator that produces a sequence of values when iterated over. They are written like regular functions but use the `yield` statement instead of `return`. The `yield` statement pauses the function, saving its state, and later continues from where it left off.

## Using the follow() Function

The `follow()` function you created previously works like the Unix `tail -f` command, which continuously monitors a file for new content. Let's use it to create a simple processing pipeline:

1. Open a new terminal window in the WebIDE (Terminal → New Terminal)

2. Start a Python interactive shell by entering:

   ```bash
   python3
   ```

3. Import the `follow` function and set up a basic pipeline to read the stock data:

   ```python
   >>> from follow import follow
   >>> import csv
   >>> lines = follow('stocklog.csv')
   >>> rows = csv.reader(lines)
   >>> for row in rows:
   ...     print(row)
   ...
   ```

4. You should see output similar to this (your data will vary):
   ```
   ['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
   ['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
   ['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
   ['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
   ...
   ```

This output shows that you've successfully created a data pipeline. The `follow()` function generates lines from the file, and these lines are then passed to the `csv.reader()` function, which parses them into rows of data.

You can stop the execution by pressing `Ctrl+C` when you've seen enough output.

## What's Happening?

In this pipeline:

1. `follow('stocklog.csv')` creates a generator that yields new lines as they're added to the file
2. `csv.reader(lines)` takes those lines and parses them into CSV row data
3. The `for` loop then iterates through these rows, printing each one

This is a simple example of a data processing pipeline using generators. In the next steps, we'll build more complex and useful pipelines.
