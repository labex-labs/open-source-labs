# 执行增量主成分分析（IPCA）

我们将通过初始化 IPCA 类的一个实例并将其拟合到数据上来对鸢尾花数据集执行增量主成分分析（IPCA）。

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
