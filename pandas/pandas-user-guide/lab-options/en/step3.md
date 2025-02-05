# Resetting Options

If we wish to reset one or more options to their default value, we can use `pd.reset_option`.

```python
# Reset the maximum display rows to default
pd.reset_option("display.max_rows")

# Verify the reset
print(pd.options.display.max_rows)
```
