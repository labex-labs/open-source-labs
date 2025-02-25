# 2番目の軸を更新する関数を定義する

第1軸に応じて第2軸を更新するためのコールバックとして登録するためのクロージャ関数を定義します。

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Update second axis according to first axis.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```
