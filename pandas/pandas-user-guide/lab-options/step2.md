# Getting and Setting Options

We can get or set the value of a single option using `pd.get_option` or `pd.set_option` respectively. Here, we are setting the maximum display rows to 999.

```python
# Get the current setting for maximum display rows
print(pd.options.display.max_rows)

# Set the maximum display rows to 999
pd.options.display.max_rows = 999

# Verify the new setting
print(pd.options.display.max_rows)
```
