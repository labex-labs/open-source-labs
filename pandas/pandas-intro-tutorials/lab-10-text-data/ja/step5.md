# 最長の名前を見つける

タイタニック号の乗客の中で最も長い名前を持つ人を見つけてみましょう。各名前の長さを取得するために`str.len()`メソッドを、最長の名前のインデックスを見つけるために`idxmax()`メソッドを使用します。

```python
# 各名前の長さを取得する
name_lengths = titanic["Name"].str.len()

# 最長の名前のインデックスを見つける
longest_name_index = name_lengths.idxmax()

# 最長の名前を取得する
longest_name = titanic.loc[longest_name_index, "Name"]
```
