# Импорт библиотек и набора данных

Сначала нам нужно импортировать необходимые библиотеки и набор данных. В этом примере мы будем использовать библиотеки `matplotlib` и `mpl_toolkits.mplot3d` для создания трехмерной диаграммы, а функцию `axes3d.get_test_data()` для генерации примера набора данных.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```
