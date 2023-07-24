# Import Libraries and Dataset

First, we need to import the necessary libraries and dataset. In this example, we will use the `matplotlib` and `mpl_toolkits.mplot3d` libraries to create the 3D plot, and the `axes3d.get_test_data()` function to generate a sample dataset.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```
