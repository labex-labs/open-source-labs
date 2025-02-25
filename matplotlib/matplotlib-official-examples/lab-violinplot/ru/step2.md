# Создаем примерный набор данных

Мы создадим примерный набор данных с использованием библиотеки numpy. Мы создадим шесть наборов данных с разными стандартными отклонениями.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```
