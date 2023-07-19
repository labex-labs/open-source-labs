# Add Arrow Annotation

Arrows can be used to point out specific features or trends in a plot. In this step, we will add an arrow to the plot that points to the maximum value.

```python
# Find the maximum value
y = [0, 1, 4, 9, 16]
max_index = y.index(max(y))
xmax = max_index
ymax = y[max_index]

# Add arrow annotation
ax.annotate('Maximum Value', xy=(xmax, ymax), xytext=(xmax, ymax + 5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```
