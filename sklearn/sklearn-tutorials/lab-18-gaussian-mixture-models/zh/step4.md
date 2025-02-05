# 对数据进行聚类

一旦模型拟合完成，我们就可以使用它对数据进行聚类，方法是将每个样本分配到它所属的高斯分量中。为此，可以使用`GaussianMixture`类的`predict`方法。

```python
# 对数据进行聚类
cluster_labels = gmm.predict(X_test)
```
