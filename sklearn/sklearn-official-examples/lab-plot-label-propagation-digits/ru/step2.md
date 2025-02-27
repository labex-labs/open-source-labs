# Подготовка данных для полусupervised обучения

Мы выбираем 340 образцов, и только 40 из этих образцов имеют известные метки. Мы сохраняем индексы оставшихся 300 образцов, для которых мы не должны знать их метки. Затем мы изменяем метки таким образом, чтобы неразмеченные образцы были помечены как -1.

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```
