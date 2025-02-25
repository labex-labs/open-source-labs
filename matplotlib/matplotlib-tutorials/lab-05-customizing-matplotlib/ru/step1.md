# Настройка rcParams во время выполнения

Вы можете динамически изменять настройки конфигурации по умолчанию во время выполнения в скрипте на Python или интерактивно из оболочки Python. Переменная `matplotlib.rcParams` является глобальной для пакета Matplotlib и хранит все настройки rc. Чтобы настроить rcParams во время выполнения, вы можете напрямую изменить ее с использованием словаря `mpl.rcParams`. Вот пример:

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

В этом коде изменяется стандартная ширина линии и стиль линии для всех графиков, создаваемых с использованием Matplotlib.

Посмотрим, как выглядят некоторые случайные данные, нарисованные с новыми настройками по умолчанию.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```
