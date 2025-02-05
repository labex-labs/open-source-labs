# 使用网格搜索计算贝叶斯岭回归的系数

```python
cv = KFold(2)  # 用于模型选择的交叉验证生成器
ridge = BayesianRidge()
cachedir = tempfile.mkdtemp()
mem = Memory(location=cachedir, verbose=1)
```
