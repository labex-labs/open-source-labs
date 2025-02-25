# 定数の定義

このステップでは、ロゴの色やフォントなどのいくつかの定数を定義します。

```python
MPL_BLUE = '#11557c'

def get_font_properties():
    # 元のフォントは Calibri ですが、インストールされていない場合は、
    # メトリック的に同等の Carlito にフォールバックします。
    if 'Calibri' in matplotlib.font_manager.findfont('Calibri:bold'):
        return matplotlib.font_manager.FontProperties(family='Calibri',
                                                      weight='bold')
    if 'Carlito' in matplotlib.font_manager.findfont('Carlito:bold'):
        print('元のフォントが見つかりません。Carlito にフォールバックします。'
              'ロゴのテキストが正しいフォントで表示されない場合があります。')
        return matplotlib.font_manager.FontProperties(family='Carlito',
                                                      weight='bold')
    print('元のフォントが見つかりません。'
          'ロゴのテキストが正しいフォントで表示されない場合があります。')
    return None
```
