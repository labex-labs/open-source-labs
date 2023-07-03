# Define the hyperparameters and evaluation metrics

In this step, we will define the hyperparameters for the DecisionTreeClassifier model and the evaluation metrics that we will be using. We will be using the AUC (Area Under the Curve) and Accuracy metrics.

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
