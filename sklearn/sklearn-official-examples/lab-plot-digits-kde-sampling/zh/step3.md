# 生成新样本

我们使用最佳估计器从数据中采样44个新点。然后，我们使用PCA的逆变换将新数据转换回其原始的64维。

```python
# 从数据中采样44个新点
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```
