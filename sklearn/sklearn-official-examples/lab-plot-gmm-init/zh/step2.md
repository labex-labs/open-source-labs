# 定义一个获取初始均值的函数

接下来，我们将定义一个函数`get_initial_means`，它以样本数据、初始化方法和随机状态作为输入，并返回初始化均值。

```python
def get_initial_means(X, init_params, r):
    # 运行一个 max_iter=0 的高斯混合模型以输出初始化均值
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
