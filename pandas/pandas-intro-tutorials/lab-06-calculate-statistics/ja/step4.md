# カテゴリ別のレコード数のカウント

最後に、カテゴリ別のレコード数をカウントします。

```python
# 各客室等級の乗客数をカウント
passengers_per_class = titanic["Pclass"].value_counts()
# 結果を表示
print(f"各客室等級の乗客数は {passengers_per_class} です")
```
