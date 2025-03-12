# Enhancing the Coroutine Pipeline

Now that we have a basic pipeline up and running, it's time to make it more flexible. In programming, flexibility is crucial as it allows our code to adapt to different requirements. We'll achieve this by modifying our `coticker.py` program to support various filtering and formatting options.

1. First, open the `coticker.py` file in your code editor. The code editor is where you'll make all the necessary changes to the program. It provides a convenient environment to view, edit, and save your code.

2. Next, we'll add a new coroutine that filters data by stock name. A coroutine is a special type of function that can pause and resume its execution. This allows us to create a pipeline where data can flow through different processing steps. Here's the code for the new coroutine:

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

In this code, the `filter_by_name` coroutine takes a stock name and a target coroutine as parameters. It continuously waits for a record using the `yield` keyword. When a record arrives, it checks if the record's name matches the specified name. If it does, it sends the record to the target coroutine.

3. Now, let's add another coroutine that filters based on price thresholds. This coroutine will help us select stocks within a specific price range. Here's the code:

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

Similar to the previous coroutine, the `price_threshold` coroutine waits for a record. It then checks if the record's price is within the specified minimum and maximum price range. If it is, it sends the record to the target coroutine.

4. After adding the new coroutines, we need to update the main program to demonstrate these additional filters. The main program is the entry point of our application, where we set up the processing pipelines and start the data flow. Here's the updated code:

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change', 'high', 'low']

    # Create the processing pipeline with multiple outputs

    # Pipeline 1: Show all negative changes (same as before)
    print("Stocks with negative changes:")
    t1 = ticker('text', fields)
    neg_filter = negchange(t1)
    tick_creator1 = create_ticker(neg_filter)
    csv_parser1 = to_csv(tick_creator1)

    # Start following the file with the first pipeline
    import threading
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser1), daemon=True).start()

    # Wait a moment to see some results
    import time
    time.sleep(5)

    # Pipeline 2: Filter by name (AAPL)
    print("\nApple stock updates:")
    t2 = ticker('text', fields)
    name_filter = filter_by_name('AAPL', t2)
    tick_creator2 = create_ticker(name_filter)
    csv_parser2 = to_csv(tick_creator2)

    # Follow the file with the second pipeline
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser2), daemon=True).start()

    # Wait a moment to see some results
    time.sleep(5)

    # Pipeline 3: Filter by price range
    print("\nStocks priced between 50 and 75:")
    t3 = ticker('text', fields)
    price_filter = price_threshold(50, 75, t3)
    tick_creator3 = create_ticker(price_filter)
    csv_parser3 = to_csv(tick_creator3)

    # Follow with the third pipeline
    follow('stocklog.csv', csv_parser3)
```

In this updated code, we create three different processing pipelines. The first pipeline shows stocks with negative changes, the second pipeline filters stocks by the name 'AAPL', and the third pipeline filters stocks based on a price range between 50 and 75. We use threads to run the first two pipelines concurrently, which allows us to process data more efficiently.

5. Once you've made all the changes, save the file. Saving the file ensures that all your modifications are preserved. Then, run the updated program using the following commands in your terminal:

```bash
cd /home/labex/project
python3 coticker.py
```

The `cd` command changes the current directory to the project directory, and the `python3 coticker.py` command runs the Python program.

6. After running the program, you should see three different outputs:
   - First, you'll see stocks with negative changes.
   - Then, you'll see all AAPL stock updates.
   - Finally, you'll see all stocks priced between 50 and 75.

## Understanding the Enhanced Pipeline

The enhanced program demonstrates several important concepts:

1. **Multiple Pipelines**: We can create multiple processing pipelines from the same data source. This allows us to perform different types of analysis on the same data simultaneously.
2. **Specialized Filters**: We can create different coroutines for specific filtering tasks. These filters help us select only the data that meets our specific criteria.
3. **Concurrent Processing**: Using threads, we can run multiple pipelines concurrently. This improves the efficiency of our program by allowing it to process data in parallel.
4. **Pipeline Composition**: Coroutines can be combined in different ways to achieve different data processing goals. This gives us the flexibility to customize our data processing pipelines according to our needs.

This approach provides a flexible and modular way to process streaming data. It allows you to add or modify processing steps without changing the overall architecture of the program.
