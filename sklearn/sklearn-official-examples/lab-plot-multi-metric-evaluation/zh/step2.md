# 加载数据集

在这一步中，我们将使用 Scikit-Learn 的 make_hastie_10_2 函数加载一个数据集。此函数生成用于二元分类的合成数据集。

```python
X, y = make_hastie_10_2(n_samples=8000, random_state=42)
```
