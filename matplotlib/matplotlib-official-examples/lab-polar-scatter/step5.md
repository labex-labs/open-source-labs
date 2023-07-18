# Create a scatter plot on a polar axis confined to a sector

We can create a scatter plot on a polar axis confined to a sector by setting the `set_thetamin()` and `set_thetamax()` methods of the `PolarAxes` object. We will set the theta start and end limits to `45` and `135`, respectively.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
