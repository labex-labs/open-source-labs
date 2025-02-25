# Импортируем библиотеки и генерируем данные

Начнем с импорта необходимых библиотек и генерации фейковых данных.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Generate fake data
np.random.seed(19680801)
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
