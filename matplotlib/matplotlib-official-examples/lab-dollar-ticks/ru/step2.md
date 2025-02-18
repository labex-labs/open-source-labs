# Создание графика

Далее, давайте создадим простой график для работы. Мы будем использовать библиотеку NumPy для генерации случайных данных для построения графика.

```python
import numpy as np

# Generate random data
np.random.seed(19680801)
data = 100 * np.random.rand(20)

# Create the plot
fig, ax = plt.subplots()
ax.plot(data)
```
