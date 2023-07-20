# Create a Bar Plot with Multiple Hatches

You can also use multiple hatches in your bar plot. In this case, we will be using an array of hatches to create multiple hatches on our bars.

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
