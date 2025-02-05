# 对随机数据进行排列检验分数计算

接下来，我们使用随机生成的特征和鸢尾花标签来计算“permutation_test_score”，这些特征和标签之间应该不存在依赖关系。

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```
