# Обучим взвешенную модель

Мы обучаем взвешенную модель с использованием того же алгоритма, что и в шаге 4, но на этот раз мы передаем аргумент sample_weight в метод fit. Затем мы строим график функции принятия решений для взвешенной модели.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
