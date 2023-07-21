# File Input and Output

Open a file.

```python
f = open('foo.txt', 'rt')     # Open for reading (text)
g = open('bar.txt', 'wt')     # Open for writing (text)
```

Read all of the data.

```python
data = f.read()

# Read only up to 'maxbytes' bytes
data = f.read([maxbytes])
```

Write some text.

```python
g.write('some text')
```

Close when you are done.

```python
f.close()
g.close()
```

Files should be properly closed and it's an easy step to forget.
Thus, the preferred approach is to use the `with` statement like this.

```python
with open(filename, 'rt') as file:
    # Use the file `file`
    ...
    # No need to close explicitly
...statements
```

This automatically closes the file when control leaves the indented code block.
