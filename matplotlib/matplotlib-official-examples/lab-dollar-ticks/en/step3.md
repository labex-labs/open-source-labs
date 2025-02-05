# Format Y-Axis Labels with Dollar Signs

Now, let's format the y-axis labels to display dollar signs. We will use the `StrMethodFormatter` class from the `matplotlib.ticker` module to format the labels.

```python
import matplotlib.ticker as ticker

# Format y-axis labels with dollar signs
fmt = '${x:,.2f}'
tick = ticker.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
```

In the above code, we create a `StrMethodFormatter` object with the format string `'$ {x:,.2f}'`. This format string specifies that we want a dollar sign followed by a space, followed by a comma-separated number with two decimal places.

Next, we create a `Tick` object using the `StrMethodFormatter` object we just created. Finally, we set the y-axis major formatter to the `Tick` object.
