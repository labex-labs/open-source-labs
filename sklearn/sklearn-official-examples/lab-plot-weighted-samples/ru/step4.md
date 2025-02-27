# Обучение моделей

Мы создадим две модели SVM. Первая модель не будет учитывать веса выборок, а вторая модель будет учитывать веса выборок, которые мы только что создали.

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
