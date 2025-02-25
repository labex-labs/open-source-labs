# グラフを変更する

選択された関数に基づいてグラフを変更する関数を定義します。この関数は、グラフ番号を入力として受け取り、それに応じてグラフを変更します。

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
