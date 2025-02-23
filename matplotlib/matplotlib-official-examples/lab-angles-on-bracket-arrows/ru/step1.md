# Импортируем необходимые библиотеки и настраиваем график

Во - первых, нам нужно импортировать необходимые библиотеки и настроить график. Мы будем использовать `matplotlib.pyplot` и `numpy`. Также создадим объект Figure и объект оси, на котором будем наносить наши данные.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots()
ax.set(xlim=(0, 6), ylim=(-1, 5))
ax.set_title("Orientation of the bracket arrows relative to angleA and angleB")
```
