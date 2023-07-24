# Import Matplotlib

Before we can start annotating plots with Matplotlib, we must first import the library. In this step, we will import Matplotlib and create a simple plot to use for annotation.

```python
import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```
