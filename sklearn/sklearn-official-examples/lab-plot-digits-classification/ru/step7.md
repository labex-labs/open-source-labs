# Восстановление отчета о классификации из матрицы ошибок

Если результаты оценки классификатора хранятся в виде матрицы ошибок, а не в виде `y_true` и `y_pred`, мы по-прежнему можем построить отчет о классификации с использованием метода `metrics.classification_report()` следующим образом:

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "Classification report rebuilt from confusion matrix:\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```
