# Exercise 4.7: Polymorphism in Action

A major feature of object-oriented programming is that you can plug an object into a program and it will work without having to change any of the existing code. For example, if you wrote a program that expected to use a `TableFormatter` object, it would work no matter what kind of `TableFormatter` you actually gave it. This behavior is sometimes referred to as "polymorphism."

One potential problem is figuring out how to allow a user to pick out the formatter that they want. Direct use of the class names such as `TextTableFormatter` is often annoying. Thus, you might consider some simplified approach. Perhaps you embed an `if-`statement into the code like this:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    print_report(report, formatter)
```

In this code, the user specifies a simplified name such as `'txt'` or `'csv'` to pick a format. However, is putting a big `if`-statement in the `portfolio_report()` function like that the best idea? It might be better to move that code to a general purpose function somewhere else.

In the `tableformat.py` file, add a function `create_formatter(name)` that allows a user to create a formatter given an output name such as `'txt'`, `'csv'`, or `'html'`. Modify `portfolio_report()` so that it looks like this:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

Try calling the function with different formats to make sure it's working.
