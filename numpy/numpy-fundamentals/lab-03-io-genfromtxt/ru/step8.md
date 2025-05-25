# Использование快捷函数

Модуль `numpy.lib.npyio` предоставляет快捷函数，полученные из `numpy.genfromtxt`. Эти функции имеют разные значения по умолчанию и возвращают либо стандартный массив NumPy, либо замаскированный массив.

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimiter=",")
```
