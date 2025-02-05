# 可视化数据集

为了更好地理解数据集，我们可以使用 matplotlib 可视化一个样本图像。以下代码显示数据集中的最后一个数字：

```python
import matplotlib.pyplot as plt

# 显示最后一个数字
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```
