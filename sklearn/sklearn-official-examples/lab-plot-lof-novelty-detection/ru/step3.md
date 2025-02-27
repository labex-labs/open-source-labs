# Обучение модели

Теперь мы обучим модель LOF с использованием обучающих данных. Мы устанавливаем количество соседей равным 20 и параметр novelty (новизна) в значение true. Также мы устанавливаем параметр contamination (загрязнение) равным 0.1.

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```
