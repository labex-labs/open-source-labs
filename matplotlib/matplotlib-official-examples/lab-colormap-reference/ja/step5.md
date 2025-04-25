# カスタムカラーマップの作成

Matplotlib は、カスタムカラーマップを作成する機能も備えています。組み込みのカラーマップがデータの望ましい表現を提供しない場合、これは便利です。

```python
import matplotlib.colors as mcolors

# Define a list of colors and their corresponding values
colors = [(0,'red'), (0.5, 'green'), (1, 'blue')]

# Create a LinearSegmentedColormap object from the list of colors
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', colors)
```
