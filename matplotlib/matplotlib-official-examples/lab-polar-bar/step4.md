# Create a polar bar chart

We will create a polar bar chart using the `projection='polar'` parameter.

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```
