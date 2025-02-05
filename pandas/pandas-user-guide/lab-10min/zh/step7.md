# 处理缺失数据

Pandas提供了处理数据框中缺失数据的方法。

```python
# 填充缺失数据
df.fillna(value=5)

# 获取值为nan的布尔掩码
pd.isna(df)
```
