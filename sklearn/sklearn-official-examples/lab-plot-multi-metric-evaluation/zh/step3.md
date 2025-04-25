# 定义超参数和评估指标

在这一步中，我们将为决策树分类器模型定义超参数以及我们将使用的评估指标。我们将使用 AUC（曲线下面积）和准确率指标。

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
