# 理解使用 DataFrame 的写时复制

现在，让我们创建一个 DataFrame，看看写时复制如何影响数据修改。

```python
# 创建一个 DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# 创建 DataFrame 的一个子集
subset = df["foo"]

# 修改子集
subset.iloc[0] = 100

# 打印原始 DataFrame
print(df)
```

## 使用 DataFrame 实现写时复制

现在，让我们看看在修改 DataFrame 时如何实现写时复制。

```python
# 启用写时复制
pd.options.mode.copy_on_write = True

# 创建 DataFrame 的一个子集
subset = df["foo"]

# 修改子集
subset.iloc[0] = 100

# 打印原始 DataFrame
print(df)
```
