# 特定の行と列を選択する

一度に行と列を選択するには、`loc` または `iloc` 演算子を使用します。

```python
# Select 'Name' of passengers older than 35
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Display the first 5 rows
adult_names.head()
```
