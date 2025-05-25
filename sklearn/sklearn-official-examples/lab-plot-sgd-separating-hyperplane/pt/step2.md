# Treinar o modelo SVM com SGD

Em seguida, precisamos treinar o modelo SVM usando SGD. Usaremos a classe `SGDClassifier` do Scikit-learn para treinar o modelo. Definiremos o parâmetro `loss` como "hinge" para usar o algoritmo SVM e o parâmetro `alpha` como 0.01 para controlar a força de regularização. Também definiremos o parâmetro `max_iter` como 200 para limitar o número de iterações.

```python
# ajustar o modelo
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```
