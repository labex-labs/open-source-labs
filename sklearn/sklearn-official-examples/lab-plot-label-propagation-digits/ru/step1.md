# Загрузка и перемешивание данных

Сначала мы загружаем набор данных с цифрами и случайным образом перемешиваем данные.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```
