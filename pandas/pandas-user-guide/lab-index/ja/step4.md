# 欠損値の処理

Pandas は、データのクリーニングと欠損値の埋め込みに様々なメソッドを提供しています。

```python
# Creating a DataFrame with missing values
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})

# Filling missing values
df.fillna(value=0, inplace=True)
```
