# カラーマップの作成

次に、クラス決定境界をプロットするためのカラーマップを作成します。背景には明るい色を、クラスの色には太い色を使用します。

```python
h = 0.05  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```
