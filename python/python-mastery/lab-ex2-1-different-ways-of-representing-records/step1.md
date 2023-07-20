# Stuck on the bus

The file `ctabus.csv` is a CSV file containing
daily ridership data for the Chicago Transit Authority (CTA) bus
system from January 1, 2001 to August 31, 2013. It contains
approximately 577000 rows of data. Use Python to view a few lines
of data to see what it looks like:

```python
>>> f = open('ctabus.csv')
>>> next(f)
'route,date,daytype,rides\n'
>>> next(f)
'3,01/01/2001,U,7354\n'
>>> next(f)
'4,01/01/2001,U,9288\n'
>>>
```

There are 4 columns of data.

- route: Column 0. The bus route name.
- date: Column 1. A date string of the form MM/DD/YYYY.
- daytype: Column 2. A day type code (U=Sunday/Holiday, A=Saturday, W=Weekday)
- rides: Column 3. Total number of riders (integer)

The `rides` column records the total number of people who boarded a
bus on that route on a given day. Thus, from the example, 7354 people
rode the number 3 bus on January 1, 2001.
