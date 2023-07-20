# Specify the Cell Size

If you need topographically accurate vertical exaggeration, or you don't want to guess at what `vert_exag` should be, you'll need to specify the cell size of the grid (i.e. the `dx` and `dy` parameters). Otherwise, any `vert_exag` value you specify will be relative to the grid spacing of your input data. In this step, we calculate the `dx` and `dy` values in meters.

```python
dy = 111200 * dy
dx = 111200 * dx * np.cos(np.radians(dem['ymin']))
```
