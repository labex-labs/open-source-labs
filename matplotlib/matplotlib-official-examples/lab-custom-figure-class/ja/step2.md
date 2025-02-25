# カスタム フィギュア サブクラスを作成する

プロットにテキスト ウォーターマークを追加する `WatermarkFigure` という名前のカスタム フィギュア サブクラスを作成します。このクラスは、Matplotlib の `Figure` クラスから継承されます。

```python
from matplotlib.figure import Figure

class WatermarkFigure(Figure):
    """A figure with a text watermark."""

    def __init__(self, *args, watermark=None, **kwargs):
        super().__init__(*args, **kwargs)

        if watermark is not None:
            bbox = dict(boxstyle='square', lw=3, ec='gray',
                        fc=(0.9, 0.9,.9,.5), alpha=0.5)
            self.text(0.5, 0.5, watermark,
                      ha='center', va='center', rotation=30,
                      fontsize=40, color='gray', alpha=0.5, bbox=bbox)
```
