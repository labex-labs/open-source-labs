# 检查内存效率

接下来，我们将检查使用稀疏数据结构的内存效率。我们将创建一个大型DataFrame，将其转换为稀疏格式，然后比较内存使用情况。

```python
# 创建一个具有随机值的大型DataFrame
df = pd.DataFrame(np.random.randn(10000, 4))

# 将DataFrame的大部分值设置为NaN
df.iloc[:9998] = np.nan

# 将DataFrame转换为稀疏格式
sdf = df.astype(pd.SparseDtype("float", np.nan))

# 检查密集型与稀疏型DataFrame的内存使用情况
print('密集型 : {:0.2f} 千字节'.format(df.memory_usage().sum() / 1e3))
print('稀疏型: {:0.2f} 千字节'.format(sdf.memory_usage().sum() / 1e3))
```
