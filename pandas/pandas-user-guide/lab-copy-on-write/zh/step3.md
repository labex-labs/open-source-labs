# 理解写时复制下的链式赋值

现在，让我们来理解链式赋值在写时复制中的工作方式。

```python
# 创建一个DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# 应用链式赋值，这将违反写时复制原则
df["foo"][df["bar"] > 5] = 100

# 打印DataFrame
print(df)
```
