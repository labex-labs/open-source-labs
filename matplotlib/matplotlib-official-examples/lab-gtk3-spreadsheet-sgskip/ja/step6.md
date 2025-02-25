# Matplotlib のプロットを作成する

このステップでは、データを表示する Matplotlib のプロットを作成します。まず、グラフを作成してサブプロットを追加します。

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```
