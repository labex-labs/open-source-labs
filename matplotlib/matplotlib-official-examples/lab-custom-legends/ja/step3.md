# さまざまな Matplotlib オブジェクトを使ったカスタム凡例の作成

このステップでは、`Line2D` や `Patch` など、さまざまな Matplotlib オブジェクトを使ってカスタム凡例を作成します。まず、`matplotlib.patches` モジュールから `Patch` クラスをインポートします。次に、カスタム属性を持つ `Line2D` と `Patch` オブジェクトのリストを作成します。最後に、カスタムオブジェクトと対応するラベルを使って `legend()` を呼び出します。

```python
# Import Line2D and Patch classes
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Create legend elements
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
                   Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Color Patch')]

# Plot data and generate custom legend
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```
