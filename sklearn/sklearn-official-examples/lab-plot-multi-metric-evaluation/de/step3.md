# Hyperparameter und Evaluationsmetriken definieren

In diesem Schritt definieren wir die Hyperparameter für das DecisionTreeClassifier-Modell und die Evaluationsmetriken, die wir verwenden werden. Wir werden die AUC (Area Under the Curve) und die Genauigkeitsmetrik verwenden.

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
