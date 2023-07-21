# Deep Idea: "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) is a computer
programming concept to determine whether an object can be used for a
particular purpose. It is an application of the [duck
test](https://en.wikipedia.org/wiki/Duck_test).

> If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

In the second version of `read_data()` above, the function expects any
iterable object. Not just the lines of a file.

```python
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records
```

This means that we can use it with other _lines_.

```python
# A CSV file
lines = open('data.csv')
data = read_data(lines)

# A zipped file
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# The Standard Input
lines = sys.stdin
data = read_data(lines)

# A list of strings
lines = ['ACME,50,91.1','IBM,75,123.45', ... ]
data = read_data(lines)
```

There is considerable flexibility with this design.

_Question: Should we embrace or fight this flexibility?_
