# Построить график данных в первом подграфике

Постройте косинус значений x в первом подграфике с использованием функции plot из matplotlib.pyplot. Используйте параметр xunits, чтобы указать, что оси x должны быть в радианах.

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
