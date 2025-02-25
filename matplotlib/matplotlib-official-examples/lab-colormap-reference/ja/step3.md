# 組み込みのカラーマップの使用

Matplotlibは、データを表現するために使用できるさまざまな組み込みのカラーマップを提供しています。これらのカラーマップは、`matplotlib.cm`モジュールにリストされている名前を使ってアクセスできます。

```python
import matplotlib.pyplot as plt

# Create a plot using the 'viridis' color map
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
