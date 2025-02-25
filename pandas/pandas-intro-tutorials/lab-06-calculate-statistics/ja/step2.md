# 要約統計量の計算

このステップでは、タイタニック号のデータセットの要約統計量を計算します。

```python
# タイタニック号の乗客の平均年齢を計算
average_age = titanic["Age"].mean()
# 結果を表示
print(f"タイタニック号の乗客の平均年齢は {average_age} です")

# タイタニック号の乗客の中央値の年齢とチケット料金を計算
median_age_fare = titanic[["Age", "Fare"]].median()
# 結果を表示
print(f"タイタニック号の乗客の中央値の年齢とチケット料金は {median_age_fare} です")
```
