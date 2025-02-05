# 理解使用DataFrame的写时复制

现在，让我们创建一个DataFrame，看看写时复制如何影响数据修改。

```python
# 创建一个DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# 创建DataFrame的一个子集
subset = df["foo"]

# 修改子集
subset.iloc[0] = 100

# 打印原始DataFrame
print(df)
```

## 使用DataFrame实现写时复制

现在，让我们看看在修改DataFrame时如何实现写时复制。

```python
# 启用写时复制
pd.options.mode.copy_on_write = True

# 创建DataFrame的一个子集
subset = df["foo"]

# 修改子集
subset.iloc[0] = 100

# 打印原始DataFrame
print(df)
```
