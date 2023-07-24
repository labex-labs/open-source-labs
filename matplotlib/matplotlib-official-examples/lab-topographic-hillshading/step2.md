# Load the Data

Next, we load the sample elevation data using the `get_sample_data` function from Matplotlib. We then extract the elevation data and the cell size of the grid.

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
