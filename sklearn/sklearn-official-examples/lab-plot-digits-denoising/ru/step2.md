# Создание обучающих и тестовых наборов

Мы разделяем набор данных на обучающий набор из 1000 образцов и тестовый набор из 100 образцов. Добавляем гауссовский шум к тестовому набору и создаем две копии исходных данных: одну с шумом и одну без шума.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise
```
