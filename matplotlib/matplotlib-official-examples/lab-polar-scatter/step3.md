# Create a scatter plot on a polar axis

We will create a scatter plot on a polar axis using the `plt.scatter()` function. We will set the `projection` parameter to `'polar'`, and pass in the radius, angle, color, and area values as parameters.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
