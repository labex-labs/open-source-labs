# Create Ellipse Collection

We create an `EllipseCollection` with the above data and specify the units to be 'x' and the offsets to be `XY`.

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
