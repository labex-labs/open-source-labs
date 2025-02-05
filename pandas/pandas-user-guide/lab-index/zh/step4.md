# 处理缺失数据

Pandas 提供了各种清理数据和填充缺失值的方法。

```python
# 创建一个带有缺失值的 DataFrame
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})

# 填充缺失值
df.fillna(value=0, inplace=True)
```
