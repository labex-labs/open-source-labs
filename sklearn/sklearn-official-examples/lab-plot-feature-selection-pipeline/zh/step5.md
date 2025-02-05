# 检查管道

我们可以检查管道以更好地理解模型。我们可以使用所选特征的索引来检索原始特征名称。

```python
anova_svm[:-1].inverse_transform(anova_svm[-1].coef_)
```
