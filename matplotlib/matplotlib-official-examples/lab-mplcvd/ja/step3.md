# メニューエントリを設定する

選択された色フィルタ名に基づいてメニューエントリを設定する関数を定義します。この関数は、選択に基づいて色フィルタ関数を更新します。

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```
