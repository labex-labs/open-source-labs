# テーブルの行をソートする

チタニック号のデータセットを、乗客の年齢に基づいてソートし、その後、客室等級と年齢で降順にソートします。

```python
# 年齢でソートする
titanic.sort_values(by="Age").head()

# 客室等級と年齢で降順にソートする
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```
