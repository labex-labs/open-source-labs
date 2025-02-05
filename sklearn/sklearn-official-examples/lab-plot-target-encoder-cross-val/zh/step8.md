# 评估无交叉验证的线性模型系数

岭回归模型出现了过拟合，因为相对于信息性特征，它给极高基数特征赋予了更多权重。运行以下代码来评估无交叉验证的线性模型系数：

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```
