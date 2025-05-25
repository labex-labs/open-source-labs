# Estabelecer um Modelo de Linha de Base

Treinaremos uma SVM linear nas características originais para estabelecer um modelo de linha de base e imprimiremos a sua precisão.

```python
from sklearn.svm import LinearSVC

# Treinar uma SVM linear nas características originais
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# Imprimir a precisão do modelo de linha de base
print(f"Precisão da SVM Linear nas características originais: {lsvm_score:.2f}%")
```
