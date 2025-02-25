# Генерация случайных данных

Мы сгенерируем два набора случайных данных с использованием NumPy. Эти данные будут использоваться для построения точечного графика.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 200)
```
