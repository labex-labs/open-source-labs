# 使用快速独立成分分析（FastICA）算法

在这一步中，我们使用快速独立成分分析（FastICA）算法，该算法在特征空间中找到与具有高非高斯性的投影相对应的方向。

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # 估计源信号

S_ica_ /= S_ica_.std(axis=0)
```
