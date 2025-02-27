# Определяем гиперпараметры и метрики оценки

В этом шаге мы определим гиперпараметры для модели DecisionTreeClassifier и метрики оценки, которые будем использовать. Будем использовать метрики AUC (Area Under the Curve) и Accuracy.

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
