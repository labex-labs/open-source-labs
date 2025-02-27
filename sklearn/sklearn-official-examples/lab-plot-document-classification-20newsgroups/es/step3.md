# Modelo con eliminación de metadatos

Ahora usaremos la opción `remove` del cargador de conjuntos de datos 20 newsgroups en scikit-learn para entrenar un clasificador de texto que no dependa demasiado de los metadatos para tomar sus decisiones. También analizaremos los errores de clasificación en un conjunto de prueba utilizando una matriz de confusión y examinaremos los coeficientes que definen la función de clasificación de los modelos entrenados.

```python
(
    X_train,
    X_test,
    y_train,
    y_test,
    feature_names,
    target_names,
) = load_dataset(remove=("headers", "footers", "quotes"))

clf = RidgeClassifier(tol=1e-2, solver="sparse_cg")
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

fig, ax = plt.subplots(figsize=(10, 5))
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax)
ax.xaxis.set_ticklabels(target_names)
ax.yaxis.set_ticklabels(target_names)
_ = ax.set_title(
    f"Matriz de confusión para {clf.__class__.__name__}\n en documentos filtrados"
)

_ = plot_feature_effects().set_title("Efectos promedio de las características en documentos filtrados")
```
