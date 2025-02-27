# Визуализируем результаты

Наконец, давайте визуализируем результаты нашей модели изотонной регрессии. Мы можем построить исходные точки данных в виде рассеянных точек, а предсказанные значения в виде линии.

```python
import matplotlib.pyplot as plt

# Plot the original data and predicted values
plt.scatter(X, y, c='b', label='Original Data')
plt.plot(X_new, y_pred, c='r', label='Isotonic Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
