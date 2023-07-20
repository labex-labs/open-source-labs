# Setting up a processing pipeline

A major power of generators is that they allow you to create programs
that set up processing pipelines--much like pipes on Unix systems.
Experiment with this concept by performing these steps:

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('Data/stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
        print(row)

['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Well, that's interesting. What you're seeing here is that the output of the
`follow()` function has been piped into the `csv.reader()` function and we're
now getting a sequence of split rows.
