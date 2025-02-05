# Create Triangulation Object

First, we need to create a Triangulation object. We will use the `Triangulation` class from `matplotlib.tri`. In this example, we will create a Triangulation object with random data.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Generate random data
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
