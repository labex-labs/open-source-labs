# Обучение модели

Мы будем обучать модель с использованием логистической регрессии с L1-штрафом и алгоритма SAGA. Мы установим значение `C` равным 50.0, разделенному на количество обучающих примеров.

```python
# Turn up tolerance for faster convergence
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
