# Обучим модель без весов

Мы обучаем модель без весов с использованием алгоритма SGDClassifier из библиотеки scikit-learn. Затем мы строим график функции принятия решений для модели без весов.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```
