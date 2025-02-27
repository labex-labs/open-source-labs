# Reconstruir el informe de clasificación a partir de la matriz de confusión

Si los resultados de la evaluación de un clasificador se almacenan en forma de una matriz de confusión y no en términos de `y_true` y `y_pred`, aún podemos construir un informe de clasificación utilizando el método `metrics.classification_report()` de la siguiente manera:

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "Informe de clasificación reconstruido a partir de la matriz de confusión:\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```
