# カラーマップの反転

Matplotlib は、カラーマップの名前に`_r`を付けることで、カラーマップを反転させる機能を備えています。

```python
import matplotlib.pyplot as plt

# Create a plot using the reversed 'viridis' color map
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```
