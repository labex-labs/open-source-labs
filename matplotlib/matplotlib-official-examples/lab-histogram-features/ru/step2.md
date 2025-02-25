# Генерируем примерные данные

В этом шаге мы сгенерируем примерные данные с использованием numpy. Мы сгенерируем случайные данные из нормального распределения с математическим ожиданием 100 и стандартным отклонением 15.

```python
np.random.seed(19680801)
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)
```
