# Setting Up

Before we start, we need to ensure that Matplotlib is installed. You can install it using pip, by running the following command:

```python
!pip install matplotlib
```

Once installed, we need to import the library and set up the environment:

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)
```
