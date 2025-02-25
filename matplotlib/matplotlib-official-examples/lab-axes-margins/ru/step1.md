# Построение графиков с отступами

Метод `margins()` в Matplotlib можно использовать для установки отступов на графике вместо методов `set_xlim()` и `set_ylim()`. В этом шаге мы узнаем, как приближать и удалять границы области просмотра на графике с использованием метода `margins()` вместо методов `set_xlim()` и `set_ylim()`.

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

# создать подграфик с отступами
ax1 = plt.subplot(212)
ax1.margins(0.05) # по умолчанию отступ равен 0.05, значение 0 означает подгонку
ax1.plot(t1, f(t1))

# создать подграфик с расширенными отступами
ax2 = plt.subplot(221)
ax2.margins(2, 2) # значения >0.0 расширяют область просмотра
ax2.plot(t1, f(t1))
ax2.set_title('Zoomed out')

# создать подграфик с приближенными отступами
ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25) # значения в (-0.5, 0.0) приближают область просмотра к центру
ax3.plot(t1, f(t1))
ax3.set_title('Zoomed in')

plt.show()
```
