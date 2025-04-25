# 从具有低浓度先验的贝叶斯高斯混合模型中采样

现在我们将从具有狄利克雷过程先验和低浓度先验值的贝叶斯高斯混合模型中进行采样。

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    0,
    "具有狄利克雷过程先验的高斯混合模型，"
    r"$\gamma_0 = 0.01$，采样 2000 个样本。",
)
```
