# タイマーオブジェクトを作成する

新しいタイマーオブジェクトを作成します。インターバルを 100 ミリ秒に設定し（デフォルトは 1000）、タイマーに何の関数を呼び出すかを指定します。

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```
