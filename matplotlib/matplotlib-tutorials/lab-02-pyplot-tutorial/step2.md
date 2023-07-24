# Formatting the Style of the Plot

Next, let's customize the style of our plot. We can use the optional third argument of the `plot` function to specify the format string, which indicates the color and line type of the plot. For example, let's plot the same line graph with red circles:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

Explanation:

- We use the format string `'ro'` to indicate red circles for the plot.
- The `axis` function is used to set the viewport of the axes, specifying the range of values for the x- and y-axis.
