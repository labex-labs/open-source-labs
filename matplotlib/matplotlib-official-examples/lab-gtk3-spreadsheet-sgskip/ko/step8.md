# 플로팅 기능 구현

이 단계에서는 행을 더블클릭했을 때 데이터를 플롯하는 기능을 구현합니다.

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```
