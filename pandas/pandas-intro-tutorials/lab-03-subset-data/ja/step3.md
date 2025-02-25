# 複数の列を選択する

複数の列を選択するには、選択角括弧 `[]` の中に列名のリストを使用します。

```python
# Select the 'Age' and 'Sex' columns
age_sex = titanic[["Age", "Sex"]]

# Display the first 5 rows
age_sex.head()
```
