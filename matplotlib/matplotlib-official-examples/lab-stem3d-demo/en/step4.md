# Customize the plot

In this step, we will customize the 3D stem plot by changing the baseline using the `bottom` parameter and changing the format using the `linefmt`, `markerfmt`, and `basefmt` parameters.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
