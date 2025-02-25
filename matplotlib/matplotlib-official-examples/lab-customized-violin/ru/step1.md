# Создание тестовых данных

Сначала мы создадим некоторые тестовые данные, которые будем использовать для violin plot. Мы будем использовать NumPy для генерации четырех массивов по 100 нормально распределенных значений с возрастающими стандартными отклонениями.

```python
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```
