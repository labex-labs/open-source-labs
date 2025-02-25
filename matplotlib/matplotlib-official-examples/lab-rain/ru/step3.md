# Построение точечного графика

Теперь мы построим точечный график, который будем обновлять в ходе анимации при развитии капель дождя.

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```
