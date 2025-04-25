# 交叉验证生成器

Scikit-learn 提供了一系列类，可用于为常见的交叉验证策略生成训练/测试索引。这些类有一个 `split` 方法，该方法接受输入数据集，并为交叉验证过程的每次迭代生成训练/测试集索引。

```python
from sklearn.model_selection import KFold

# 使用 KFold 交叉验证将数据拆分为 K 折
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'训练集：{train_indices} | 测试集：{test_indices}')
```

`cross_val_score` 辅助函数可用于直接计算交叉验证分数。它在交叉验证的每次迭代中将数据拆分为训练集和测试集，在训练集上训练估计器，并根据测试集计算分数。

```python
from sklearn.model_selection import cross_val_score

# 计算支持向量机分类器的交叉验证分数
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```
