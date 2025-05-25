# Criar Classificador SVM

Neste passo, criaremos uma instância do classificador SVM e ajustaremos nossos dados. Usaremos o kernel personalizado criado no passo anterior.

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```
