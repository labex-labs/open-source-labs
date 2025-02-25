# Построить график данных во втором подграфике

Постройте косинус значений x во втором подграфике с использованием функции plot из matplotlib.pyplot. Используйте параметр xunits, чтобы указать, что оси x должны быть в градусах.

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
