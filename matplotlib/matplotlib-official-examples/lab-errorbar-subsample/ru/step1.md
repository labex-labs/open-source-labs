# Импорт библиотек и генерация данных

Во - первых, нам нужно импортировать необходимые библиотеки и сгенерировать некоторые примерные данные для работы. В этом примере мы будем использовать numpy для генерации данных и matplotlib для их визуализации.

```python
import matplotlib.pyplot as plt
import numpy as np

# example data
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# example variable error bar values
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
