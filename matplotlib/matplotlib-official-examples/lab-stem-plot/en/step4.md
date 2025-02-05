# Customizing the Plot

We can customize the plot by adjusting the baseline using the `bottom` parameter. We can also adjust the format properties of the plot using the `linefmt`, `markerfmt`, and `basefmt` parameters.

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

This will generate a plot with a grey line format and diamond-shaped markers. The baseline has also been adjusted to 1.1.
