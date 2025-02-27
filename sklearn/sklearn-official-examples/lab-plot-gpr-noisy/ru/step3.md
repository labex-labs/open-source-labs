# Добавление шума

В этом шаге мы добавим некоторый шум к сгенерированным данным, чтобы создать более реалистичный набор данных для обучения.

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```
