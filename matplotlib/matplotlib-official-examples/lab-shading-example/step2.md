# Load Data

Next, we will load the sample data that we will use for this tutorial. We will use the `jacksboro_fault_dem.npz` file, which contains elevation data.

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
