# Criar o Modelo

Neste passo, criaremos o modelo SVM-Kernel com três núcleos diferentes: linear, polinomial e de função de base radial (RBF). O núcleo linear é usado para pontos de dados linearmente separáveis, enquanto os núcleos polinomial e RBF são úteis para pontos de dados não linearmente separáveis.

```python
# ajustar o modelo
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```
