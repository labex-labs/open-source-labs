# Переупорядочиваем перемешанный набор данных

Мы переупорядочиваем перемешанный набор данных, чтобы сделать бикластеры непрерывными, используя функцию `argsort()` из библиотеки numpy.

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
