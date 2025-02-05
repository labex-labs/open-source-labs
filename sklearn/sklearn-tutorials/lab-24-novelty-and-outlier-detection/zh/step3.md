# 创建一个异常值检测估计器

现在，我们可以从`neighbors.LocalOutlierFactor`类创建一个异常值检测估计器对象。这个类实现了局部异常因子（Local Outlier Factor）算法，这是一种流行的异常值检测方法。

```python
estimator = neighbors.LocalOutlierFactor()
```
