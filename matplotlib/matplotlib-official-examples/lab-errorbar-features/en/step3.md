# Define Error Values

We will now define our error values. In this example, we will use the `error` variable to represent symmetric error and the `asymmetric_error` variable to represent asymmetric error.

```python
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x

# error bar values w/ different -/+ errors that
# also vary with the x-position
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
