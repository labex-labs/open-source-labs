# Customizing the Chart

We can customize the appearance of our chart by adding labels to the x-axis and y-axis, and by setting the scale of the y-axis to logarithmic.

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
