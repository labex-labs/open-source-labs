# Генерация данных

Мы сгенерируем данные с использованием NumPy. Мы сгенерируем 100 точек данных с равномерным распределением между 0 и 5. Мы установим порог в 2,5 и сгенерируем метки с использованием булевого выражения. Мы будем использовать первые 50 точек данных в качестве обучающих данных, а оставшиеся - в качестве тестовых данных.

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
