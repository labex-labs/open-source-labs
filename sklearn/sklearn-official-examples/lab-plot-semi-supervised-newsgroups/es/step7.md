# Entrenar y evaluar el modelo de LabelSpreading

En este paso, utilizaremos LabelSpreading en el 20% de los datos etiquetados. Seleccionaremos al azar el 20% de los datos etiquetados, entrenaremos el modelo con esos datos y luego usaremos el modelo para predecir las etiquetas para el resto de los datos no etiquetados.

```python
# Entrenar y evaluar el pipeline de LabelSpreading
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
