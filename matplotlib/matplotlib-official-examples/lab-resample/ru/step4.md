# Обновление данных

Мы определим метод `update`, который будет обновлять данные. Метод будет принимать ax (ось) в качестве входного параметра. Мы обновим линию, получив пределы просмотра и проверив, отличается ли ширина пределов просмотра от delta. Если ширина пределов просмотра отличается от delta, мы обновим delta и получим xstart и xend. Затем мы установим данные в уменьшенные по частоте дискретизации данные и нарисуем холст холста в состоянии покоя.

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```
