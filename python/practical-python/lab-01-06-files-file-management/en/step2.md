# Common Idioms for Reading File Data

Read an entire file all at once as a string.

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` is a string with all the text in `foo.txt`
```

Read a file line-by-line by iterating.

```python
with open(filename, 'rt') as file:
    for line in file:
        # Process the line
```
