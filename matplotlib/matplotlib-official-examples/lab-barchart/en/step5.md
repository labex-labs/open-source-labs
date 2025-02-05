# Customize the Chart

We can customize the chart by adding labels, a title, and adjusting the x-axis tick labels and legend. We will also set the y-axis limit to ensure that all of our data is visible.

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```
