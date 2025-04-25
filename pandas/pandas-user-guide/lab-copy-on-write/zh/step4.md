# 使用写时复制实现链式赋值

最后，让我们看看如何使用`loc`方法在写时复制的情况下实现链式赋值。

```python
# 创建一个 DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# 使用'loc'在写时复制的情况下应用链式赋值
df.loc[df["bar"] > 5, "foo"] = 100

# 打印 DataFrame
print(df)
```
