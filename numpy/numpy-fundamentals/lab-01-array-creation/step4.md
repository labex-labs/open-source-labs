# Reading Arrays from Disk

You can read arrays from disk in various formats. For standard binary formats, there are Python libraries like h5py for HDF5 and Astropy for FITS. For common ASCII formats like CSV and TSV, you can use the `np.loadtxt` and `np.genfromtxt` functions. Here's an example of reading a CSV file:

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
