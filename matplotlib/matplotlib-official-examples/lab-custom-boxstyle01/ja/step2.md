# クラスとしてカスタムボックススタイルを実装する

カスタムボックススタイルは、`__call__` を実装するクラスとしても実装できます。その後、これらのクラスを `BoxStyle._style_list` 辞書に登録することができ、これにより、ボックススタイルを文字列として指定できます。`bbox=dict(boxstyle="登録名,param=値,...",...)` です。

```python
class MyStyle:
    """シンプルなボックス。"""

    def __init__(self, pad=0.3):
        """
        引数は浮動小数点数で、デフォルト値を持っている必要があります。

        パラメータ
        ----------
        pad : float
            パディング量
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        ボックスの位置とサイズを指定すると、その周りのボックスのパスを返します。

        回転は自動的に処理されます。

        パラメータ
        ----------
        x0, y0, width, height : float
            ボックスの位置とサイズ。
        mutation_size : float
            変異の基準スケール、通常はテキストのフォントサイズ。
        """
        # パディング
        pad = mutation_size * self.pad
        # パディングを加えた幅と高さ
        width = width + 2.*pad
        height = height + 2.*pad
        # パディング付きボックスの境界
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # 新しいパスを返す
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # カスタムスタイルを登録します。

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # 登録解除します。

plt.show()
```
