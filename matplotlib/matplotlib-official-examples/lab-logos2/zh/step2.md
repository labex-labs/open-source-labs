# 定义常量

在这一步中，我们将定义一些常量，包括徽标的颜色和字体。

```python
MPL_BLUE = '#11557c'

def get_font_properties():
    # 原始字体是 Calibri，如果未安装该字体，我们将回退到 Carlito，它在度量上是等效的。
    if 'Calibri' in matplotlib.font_manager.findfont('Calibri:bold'):
        return matplotlib.font_manager.FontProperties(family='Calibri',
                                                      weight='bold')
    if 'Carlito' in matplotlib.font_manager.findfont('Carlito:bold'):
        print('未找到原始字体。回退到 Carlito。徽标文本的字体将不正确。')
        return matplotlib.font_manager.FontProperties(family='Carlito',
                                                      weight='bold')
    print('未找到原始字体。徽标文本的字体将不正确。')
    return None
```
