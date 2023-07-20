# Add Error Bars to the Plot

We add error bars to our plot using the `errorbar` method of the `Axes3D` object. We set the `zuplims` and `zlolims` parameters to arrays that specify which data points have upper and lower limits. We set the `errorevery` parameter to control the frequency of error bars.

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```
