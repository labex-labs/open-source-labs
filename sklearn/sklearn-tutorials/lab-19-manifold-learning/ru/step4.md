# Сравните результаты

Сравните результаты различных алгоритмов обучения многообразия. Визуализируйте преобразованные данные, чтобы увидеть, как алгоритмы сохранили основную структуру данных.

```python
import matplotlib.pyplot as plt

# Создайте диаграмму рассеяния преобразованных данных
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('Manifold Learning')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()
```
