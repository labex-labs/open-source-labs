# 创建颜色映射

现在我们将创建颜色映射，用于绘制类别决策边界。我们将使用浅色作为背景，使用鲜明的颜色作为类别颜色。

```python
h = 0.05  # 网格中的步长

# 创建颜色映射
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```
