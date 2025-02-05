# Data Analysis Challenge

In the last lab you just wrote some code to read CSV-data related to the Chicago Transit Authority. For example, you can grab the data as dictionaries like this:

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>>
```

It would be a shame to do all of that work and then do nothing with the data.

In this exercise, you task is this: write a program to answer the following four questions:

1.  How many bus routes exist in Chicago?

2.  How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?

3.  What is the total number of rides taken on each bus route?

4.  What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

You are free to use any technique whatsoever to answer the above questions as long as it's part of the Python standard library (i.e., built-in datatypes, standard library modules, etc.).
