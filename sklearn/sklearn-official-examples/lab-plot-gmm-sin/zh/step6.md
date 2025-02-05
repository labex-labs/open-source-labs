# 绘制具有低浓度先验的贝叶斯高斯混合模型的结果

我们将绘制具有狄利克雷过程先验和低浓度先验值的贝叶斯高斯混合模型的结果。

```python
plot_results(
    X,
    dpgmm.predict(X),
    dpgmm.means_,
    dpgmm.covariances_,
    1,
    "具有狄利克雷过程先验的贝叶斯高斯混合模型，"
    r"$\gamma_0 = 0.01$。",
)
```
