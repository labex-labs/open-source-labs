# Ajustar o Modelo Ponderado

Ajustamos um modelo ponderado utilizando o mesmo algoritmo do Passo 4, mas desta vez passamos o argumento `sample_weight` para o método `fit`. Em seguida, plotamos a função de decisão do modelo ponderado.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
