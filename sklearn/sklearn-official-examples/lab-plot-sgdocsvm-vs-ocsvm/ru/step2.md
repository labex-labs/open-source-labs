# Генерация данных

Для этого практического занятия мы сгенерируем небольшой набор данных. Мы сгенерируем 500 тренировочных образцов и 20 тестовых образцов. Также сгенерируем 20 аномальных образцов.

```python
random_state = 42
rng = np.random.RandomState(random_state)

# Generate train data
X = 0.3 * rng.randn(500, 2)
X_train = np.r_[X + 2, X - 2]
# Generate some regular novel observations
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# Generate some abnormal novel observations
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
```
