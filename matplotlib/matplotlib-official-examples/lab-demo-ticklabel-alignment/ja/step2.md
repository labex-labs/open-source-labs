# グリッド設定用の関数を定義する

コードを簡略化するために、グラフオブジェクトと位置を入力として受け取り、カスタム目盛りラベル付きのグリッドオブジェクトを返す関数を定義できます。

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8], labels=["short", "loooong"])
    ax.set_xticks([0.2, 0.8], labels=[r"$\frac{1}{2}\pi$", r"$\pi$"])
    return ax
```
