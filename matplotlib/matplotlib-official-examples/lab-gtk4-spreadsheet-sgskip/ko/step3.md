# 데이터 플롯

이제 트리뷰의 항목을 더블 클릭하여 데이터를 플롯합니다.

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
