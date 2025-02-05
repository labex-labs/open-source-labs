# Create a scatter plot on a polar axis with offset origin

We can create a scatter plot on a polar axis with an offset origin by setting the `set_rorigin()` and `set_theta_zero_location()` methods of the `PolarAxes` object. We will set the origin radius to `-2.5` and the theta zero location to `'W'` with an offset of `10`.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
