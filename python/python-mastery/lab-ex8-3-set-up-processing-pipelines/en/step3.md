# Enhancing the Coroutine Pipeline

Now that we have a basic pipeline working, let's enhance it by adding more flexibility to our pipeline. We'll modify our `coticker.py` program to allow different filtering and formatting options.

1. Open the `coticker.py` file in the code editor.

2. Add a new coroutine that filters by stock name:

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

3. Add another coroutine that filters based on price thresholds:

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

4. Now, update the main program to demonstrate these additional filters:

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

5. Save the file and run the updated program:

```bash
cd /home/labex/project
python3 coticker.py
```

6. You should see three different outputs:
   - First, stocks with negative changes
   - Then, all AAPL stock updates
   - Finally, all stocks priced between 50 and 75

## Understanding the Enhanced Pipeline

The enhanced program demonstrates several important concepts:

1. **Multiple Pipelines**: We can create multiple processing pipelines from the same data source.

2. **Specialized Filters**: We can create different coroutines for specific filtering tasks.

3. **Concurrent Processing**: Using threads, we can run multiple pipelines concurrently.

4. **Pipeline Composition**: Coroutines can be combined in different ways to achieve different data processing goals.

This approach provides a flexible and modular way to process streaming data, allowing you to add or modify processing steps without changing the overall architecture.
