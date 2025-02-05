# Customize the Chart

To make the chart more informative, we can customize it by adding labels, title, and by inverting the y-axis.

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
