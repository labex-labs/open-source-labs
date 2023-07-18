# Generating a Simple Plot

To start, let's generate a simple plot using the `plot` function in `pyplot`. In this example, we'll plot a line graph with the y-values `[1, 2, 3, 4]`:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

Explanation:

- We import the `pyplot` module from `matplotlib` and alias it as `plt`.
- The `plot` function is used to generate a line graph. By providing a single list of y-values, the x-values are automatically generated as `[0, 1, 2, 3]`, since Python ranges start with 0.
- The `ylabel` function sets the label for the y-axis.
- Finally, the `show` function displays the plot.
