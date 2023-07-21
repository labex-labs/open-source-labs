# Prefer keyword arguments for optional arguments

Compare and contrast these two different calling styles:

```python
parse_data(data, False, True) # ?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

In most cases, keyword arguments improve code clarity--especially for arguments that
serve as flags or which are related to optional features.
