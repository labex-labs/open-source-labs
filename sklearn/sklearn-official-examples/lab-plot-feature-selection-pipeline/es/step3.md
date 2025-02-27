# Entrenar la Canalización

Ahora entrenaremos la canalización en el subconjunto de entrenamiento utilizando el método `fit`. Durante el entrenamiento, la función `SelectKBest` seleccionará las 3 características más informativas basadas en el valor F de ANOVA, y la función `LinearSVC` entrenará un clasificador SVM lineal en las características seleccionadas.

```python
anova_svm.fit(X_train, y_train)
```
