# Импортируем библиотеки и генерируем данные

Во - первых, нам нужно импортировать необходимые библиотеки и сгенерировать некоторые данные для построения графика. В этом примере мы будем использовать нормальное распределение для генерации данных для оси y.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
```
