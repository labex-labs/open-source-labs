# Producer-Consumer Problems

Generators are closely related to various forms of _producer-consumer_ problems.

```python
# Producer
def follow(f):
    ...
    while True:
        ...
        yield line        # Produces value in `line` below
        ...

# Consumer
for line in follow(f):    # Consumes value from `yield` above
    ...
```

`yield` produces values that `for` consumes.
