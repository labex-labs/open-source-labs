# 可视化特征排名

最后，我们将使用 Matplotlib 库绘制特征排名。我们将使用 `matshow()` 函数将排名显示为图像。我们还将为绘图添加颜色条和标题。

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
```
