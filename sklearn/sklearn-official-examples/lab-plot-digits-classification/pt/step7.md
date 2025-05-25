# Reconstruir o Relatório de Classificação a Partir da Matriz de Confusão

Se os resultados da avaliação de um classificador forem armazenados na forma de uma matriz de confusão, e não em termos de `y_true` e `y_pred`, ainda podemos construir um relatório de classificação usando o método `metrics.classification_report()` da seguinte forma:

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "Relatório de classificação reconstruído a partir da matriz de confusão:\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```
