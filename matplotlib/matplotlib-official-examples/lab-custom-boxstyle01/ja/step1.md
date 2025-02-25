# 関数としてカスタムボックススタイルを実装する

カスタムボックススタイルは、長方形のボックスと「変異」量を指定する引数を受け取り、「変異」されたパスを返す関数として実装できます。ここでは、ボックスの左側に「矢印」形状を追加した新しいパスを返すカスタムボックススタイルを実装します。

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    ボックスの位置とサイズを指定すると、その周りのボックスのパスを返します。

    回転は自動的に処理されます。

    パラメータ
    ----------
    x0, y0, width, height : float
        ボックスの位置とサイズ。
    mutation_size : float
        変異基準スケール、通常はテキストのフォントサイズ。
    """
    # パディング
    mypad = 0.3
    pad = mutation_size * mypad
    # パディングを加えた幅と高さ。
    width = width + 2 * pad
    height = height + 2 * pad
    # パディング付きボックスの境界
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # 新しいパスを返す
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```
