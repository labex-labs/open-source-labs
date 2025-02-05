# 评估聚类

为了评估聚类结果，我们可以计算聚类的惯性，它表示样本到其最近聚类中心的平方距离之和。

```python
# 计算聚类的惯性
inertia = kmeans.inertia_
print("Inertia:", inertia)
```
