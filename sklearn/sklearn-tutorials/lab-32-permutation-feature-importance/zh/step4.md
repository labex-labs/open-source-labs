# 计算排列特征重要性

现在，我们将使用 scikit-learn 中的`permutation_importance`函数来计算排列特征重要性。此函数将训练好的模型、验证集以及特征应被置换的次数作为输入。

```python
from sklearn.inspection import permutation_importance

# 计算排列特征重要性
result = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0)

# 打印特征重要性
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{diabetes.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
