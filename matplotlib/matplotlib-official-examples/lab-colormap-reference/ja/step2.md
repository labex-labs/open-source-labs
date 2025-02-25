# 単純なカラーマップの作成

単純なカラーマップを作成するには、`matplotlib.colors`モジュールの`ListedColormap`クラスを使うことができます。このクラスは色のリストを受け取り、それらからカラーマップを作成します。

```python
import matplotlib.colors as mcolors

# Define a list of colors
colors = ['red', 'green', 'blue']

# Create a ListedColormap object from the list of colors
cmap = mcolors.ListedColormap(colors)
```
