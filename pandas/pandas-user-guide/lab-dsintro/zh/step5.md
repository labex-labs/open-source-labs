# 数据对齐与算术运算

数据对齐是 pandas 的一项重要特性。当你对两个对象执行操作时，pandas 会根据它们相关联的标签进行对齐。

```python
# 创建两个 DataFrame
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# 执行加法运算
result = df1 + df2
```
