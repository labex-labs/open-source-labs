# カスタム凡例の作成

このステップでは、Matplotlibオブジェクトを使ってカスタム凡例を作成します。まず、`matplotlib.lines` モジュールから `Line2D` クラスをインポートします。次に、色、幅、ラベル属性を持つ `Line2D` オブジェクトのリストを作成します。最後に、`plot` 関数を使って再びデータを描画し、カスタムの線と対応するラベルを使って `legend()` を呼び出します。

```python
# Import Line2D class
from matplotlib.lines import Line2D

# Create custom lines
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Plot data and generate custom legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
