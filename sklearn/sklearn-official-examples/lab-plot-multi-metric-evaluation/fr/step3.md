# Définir les hyperparamètres et les métriques d'évaluation

Dans cette étape, nous allons définir les hyperparamètres pour le modèle DecisionTreeClassifier et les métriques d'évaluation que nous allons utiliser. Nous utiliserons les métriques AUC (Area Under the Curve) et Accuracy.

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
