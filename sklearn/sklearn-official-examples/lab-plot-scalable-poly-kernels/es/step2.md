# Establecer un Modelo de Referencia

Entrenaremos un SVM lineal en las características originales para establecer un modelo de referencia y mostrar su precisión.

```python
from sklearn.svm import LinearSVC

# Entrenar un SVM lineal en las características originales
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# Mostrar la precisión del modelo de referencia
print(f"Linear SVM score on raw features: {lsvm_score:.2f}%")
```
