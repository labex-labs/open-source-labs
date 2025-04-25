# MenuItem クラスを定義する

次に、メニュー内の各項目を作成するために使用される`MenuItem`クラスを定義します。このクラスには、グラフ、ラベル文字列、プロパティ、ホバー時のプロパティ、および選択時のコールバック関数をパラメータとして渡します。`MenuItem`クラスは`artist.Artist`クラスから継承されています。

```python
class MenuItem(artist.Artist):
    padx = 5
    pady = 5

    def __init__(self, fig, labelstr, props=None, hoverprops=None,
                 on_select=None):
        super().__init__()

        self.set_figure(fig)
        self.labelstr = labelstr

        self.props = props if props is not None else ItemProperties()
        self.hoverprops = (
            hoverprops if hoverprops is not None else ItemProperties())
        if self.props.fontsize!= self.hoverprops.fontsize:
            raise NotImplementedError(
               'support for different font sizes not implemented')

        self.on_select = on_select

        # IdentityTransform() に変換を設定することで、
        # 座標を直接ピクセル単位で指定できます。
        self.label = fig.text(0, 0, labelstr, transform=IdentityTransform(),
                              size=props.fontsize)
        self.text_bbox = self.label.get_window_extent(
            fig.canvas.get_renderer())

        self.rect = patches.Rectangle((0, 0), 1, 1)  # 後で更新されます。

        self.set_hover_props(False)

        fig.canvas.mpl_connect('button_release_event', self.check_select)

    def check_select(self, event):
        over, _ = self.rect.contains(event)
        if not over:
            return
        if self.on_select is not None:
            self.on_select(self)

    def set_extent(self, x, y, w, h, depth):
        self.rect.set(x=x, y=y, width=w, height=h)
        self.label.set(position=(x + self.padx, y + depth + self.pady/2))
        self.hover = False

    def draw(self, renderer):
        self.rect.draw(renderer)
        self.label.draw(renderer)

    def set_hover_props(self, b):
        props = self.hoverprops if b else self.props
        self.label.set(color=props.labelcolor)
        self.rect.set(facecolor=props.bgcolor, alpha=props.alpha)

    def set_hover(self, event):
        """
        イベントのホバー状態を更新し、変更されたかどうかを返します。
        """
        b, _ = self.rect.contains(event)
        changed = (b!= self.hover)
        if changed:
            self.set_hover_props(b)
        self.hover = b
        return changed
```
