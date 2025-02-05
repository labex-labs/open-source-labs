# 使用内置颜色映射表

Matplotlib提供了各种可用于表示数据的内置颜色映射表。这些颜色映射表可以通过它们在 `matplotlib.cm` 模块中列出的名称来访问。

```python
import matplotlib.pyplot as plt

# 使用 'viridis' 颜色映射表创建一个绘图
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
