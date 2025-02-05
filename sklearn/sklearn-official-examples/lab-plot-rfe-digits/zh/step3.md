# 对特征进行排序

将数据拟合到 RFE 对象之后，我们可以根据特征的重要性对其进行排序。我们将使用 RFE 对象的 `ranking_` 属性来获取特征排名。我们还将重塑排名，使其与原始图像的形状相匹配。

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```
