# Keep going

Oh, you can do better than that. Let's plug this into your table generation code. Change
the program to the following:

```python
# ticker.py
...

if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name','price','change'], formatter)
```

This should produce some output that looks like this:

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

Now, THAT is crazy! And pretty awesome.

**Discussion**

Some lessons learned: You can create various generator functions and
chain them together to perform processing involving data-flow
pipelines.

A good mental model for generator functions might be Lego blocks.
You can make a collection of small iterator patterns and start
stacking them together in various ways. It can be an extremely powerful way to program.
