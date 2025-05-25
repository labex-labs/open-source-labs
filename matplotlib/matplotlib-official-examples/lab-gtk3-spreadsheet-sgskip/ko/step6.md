# Matplotlib 플롯 생성

이 단계에서는 데이터를 표시할 Matplotlib 플롯을 생성합니다. 먼저 figure 를 생성하고 subplot 을 추가하는 것으로 시작합니다.

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```
