# Reading a portfolio

Add a function `read_portfolio()` to your `stock.py` program that
reads a file of portfolio data into a list of `Stock` objects. Here's how it should work:

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> for s in portfolio:
        print(s)

<__main__.Stock object at 0x3902f0>
<__main__.Stock object at 0x390270>
<__main__.Stock object at 0x390330>
<__main__.Stock object at 0x390370>
<__main__.Stock object at 0x3903b0>
<__main__.Stock object at 0x3903f0>
<__main__.Stock object at 0x390430>
>>>
```

You already wrote a similar function as part of
[Exercise 2.3](ex2_3.md). Design discussion: Should
`read_portfolio()` be a separate function or part of the class
definition?
