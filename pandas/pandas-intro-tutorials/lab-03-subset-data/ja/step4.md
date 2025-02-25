# 特定の行をフィルタリングする

条件式に基づいて行を選択するには、選択角括弧 `[]` の中に条件を使用します。

```python
# Filter rows where 'Age' is greater than 35
above_35 = titanic[titanic["Age"] > 35]

# Display the first 5 rows
above_35.head()
```
