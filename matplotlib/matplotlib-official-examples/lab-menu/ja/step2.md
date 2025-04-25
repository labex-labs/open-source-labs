# ItemProperties クラスを定義する

次に、各メニュー項目のプロパティを設定するために使用される`ItemProperties`クラスを定義します。このクラスを使用することで、各項目のフォントサイズ、ラベル色、背景色、およびアルファ値を設定できます。

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
