# Enabling Copy-On-Write

First, let's enable CoW in pandas. This can be done using the `copy_on_write` configuration option in pandas. Here are two ways you can enable CoW globally.

```python
# Enable CoW using set_option
pd.set_option("mode.copy_on_write", True)

# Or using direct assignment
pd.options.mode.copy_on_write = True
```
