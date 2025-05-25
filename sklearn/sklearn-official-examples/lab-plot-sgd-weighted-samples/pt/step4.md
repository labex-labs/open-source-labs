# Ajustar o Modelo Sem Pesos

Ajustamos um modelo sem pesos utilizando o algoritmo SGDClassifier da biblioteca scikit-learn. Em seguida, plotamos a função de decisão do modelo sem pesos.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```
