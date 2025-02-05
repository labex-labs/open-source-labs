# 初始化投票分类器

然后，我们将使用权重 `[1, 1, 5]` 初始化一个软投票的 VotingClassifier，这意味着在计算平均概率时，RandomForestClassifier 的预测概率的权重是其他分类器权重的 5 倍。

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```
