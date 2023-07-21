# Indentation best practices

- Use spaces instead of tabs.
- Use 4 spaces per level.
- Use a Python-aware editor.

Python's only requirement is that indentation within the same block
be consistent. For example, this is an error:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # ERROR
    num_bills = num_bills * 2
```
