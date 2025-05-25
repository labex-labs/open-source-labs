# 플롯 변경

선택된 함수에 따라 플롯을 변경하는 함수를 정의합니다. 이 함수는 plot_number 를 입력으로 받아 플롯을 적절하게 변경합니다.

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
