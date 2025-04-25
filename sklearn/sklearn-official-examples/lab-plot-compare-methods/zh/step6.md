# T 分布随机邻域嵌入

它将数据点之间的相似度转换为联合概率，并试图最小化低维嵌入的联合概率与高维数据的联合概率之间的库尔贝克 - 莱布勒散度（Kullback-Leibler divergence）。

```python
t_sne = manifold.TSNE(
    n_components=n_components,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)
```
