# Mapping

One of the most common operations in functional programming is the `map()` operation that maps a function
to the values in a sequence. Python has a built-in `map()` function that does this. For
example:

```python
>>> nums = [1,2,3,4]
>>> squares = map(lambda x: x*x, nums)
>>> for n in squares:
        print(n)

1
4
9
16
>>>
```

`map()` produces an iterator so if you want a list, you'll need to create it explicitly:

```python
>>> squares = list(map(lambda x: x*x, nums))
>>> squares
[1, 4, 9, 16]
>>>
```

Try to use `map()` in your `convert_csv()` function.
