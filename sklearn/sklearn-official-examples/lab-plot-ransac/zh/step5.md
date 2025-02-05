# 比较估计系数

我们将比较真实模型、线性模型和 RANSAC 回归器的估计系数。

```python
# 比较估计系数
print("估计系数 (真实、线性回归、RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
