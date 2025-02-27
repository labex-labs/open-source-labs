# ハイパーパラメータと評価指標の定義

このステップでは、DecisionTreeClassifier モデルのハイパーパラメータと使用する評価指標を定義します。AUC（曲線下の面積）と正解率の指標を使用します。

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
