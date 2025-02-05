# 创建虚拟变量

你可以使用`get_dummies`方法从字符串数据创建虚拟变量。

```python
# 创建虚拟变量
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```
