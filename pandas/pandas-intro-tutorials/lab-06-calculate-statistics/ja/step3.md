# カテゴリ別に集計した統計量

次に、カテゴリ別に集計した統計量を学びます。

```python
# タイタニック号の男性と女性の乗客の平均年齢を計算
average_age_sex = titanic[["Sex", "Age"]].groupby("Sex").mean()
# 結果を表示
print(f"タイタニック号の男性と女性の乗客の平均年齢は {average_age_sex} です")

# 性別と客室等級の各組み合わせごとの平均チケット料金を計算
mean_fare_sex_class = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
# 結果を表示
print(f"性別と客室等級の各組み合わせごとの平均チケット料金は {mean_fare_sex_class} です")
```
