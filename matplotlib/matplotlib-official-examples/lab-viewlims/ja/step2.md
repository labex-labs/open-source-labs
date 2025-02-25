# UpdatingRect クラスを作成する

Rectangle のサブクラスである UpdatingRect を作成します。このクラスは Axes インスタンスを引数に呼び出されると、矩形の形状を Axes の範囲に合わせて更新します。

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
