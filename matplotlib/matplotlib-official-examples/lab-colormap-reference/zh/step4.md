# 反转颜色映射表

Matplotlib提供了通过在颜色映射表名称后附加 `_r` 来反转颜色映射表的功能。

```python
import matplotlib.pyplot as plt

# 使用反转后的 'viridis' 颜色映射表创建一个绘图
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```
