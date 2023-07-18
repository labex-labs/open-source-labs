# Using option_context

The `option_context` function allows us to execute a code block with a set of options that revert to prior settings after execution.

```python
# Execute a code block with a set of options
with pd.option_context("display.max_rows", 10):
    # This will print 10 despite the global setting being different
    print(pd.get_option("display.max_rows"))

# This will print the global setting as the context block has ended
print(pd.get_option("display.max_rows"))
```
