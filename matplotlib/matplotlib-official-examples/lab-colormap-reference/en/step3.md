# Using Built-In Color Maps

Matplotlib provides a variety of built-in color maps that can be used to represent data. These color maps can be accessed using their names, which are listed in the `matplotlib.cm` module.

```python
import matplotlib.pyplot as plt

# Create a plot using the 'viridis' color map
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
