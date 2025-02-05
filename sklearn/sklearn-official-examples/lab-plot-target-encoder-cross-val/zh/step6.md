# 使用交叉验证评估线性模型的系数

线性模型的系数表明，大部分权重都在列索引为 0 的特征上，即信息性特征。运行以下代码以使用交叉验证评估线性模型的系数：

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```
