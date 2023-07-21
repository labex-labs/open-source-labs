# Reversing Color Maps

Matplotlib provides the ability to reverse a color map by appending `_r` to the name of the color map.

```python
import matplotlib.pyplot as plt

# Create a plot using the reversed 'viridis' color map
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```
