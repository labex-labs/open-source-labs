# タイトルを更新する関数を定義する

グラフのタイトルを現在時刻で更新する関数を定義します。

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
