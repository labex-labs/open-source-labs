# Rebâtir le rapport de classification à partir de la matrice de confusion

Si les résultats de l'évaluation d'un classifieur sont stockés sous forme d'une matrice de confusion et non en termes de `y_true` et `y_pred`, nous pouvons toujours construire un rapport de classification en utilisant la méthode `metrics.classification_report()` comme suit :

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "Rapport de classification reconstruit à partir de la matrice de confusion :\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```
