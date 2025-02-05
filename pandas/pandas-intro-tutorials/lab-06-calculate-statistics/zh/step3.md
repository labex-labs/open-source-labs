# 按类别分组聚合统计信息

接下来，我们将学习如何按类别分组聚合统计信息。

```python
# 计算泰坦尼克号男性和女性乘客的平均年龄
average_age_sex = titanic[["Sex", "Age"]].groupby("Sex").mean()
# 打印结果
print(f"泰坦尼克号男性和女性乘客的平均年龄是 {average_age_sex}")

# 计算每种性别和客舱等级组合的平均票价
mean_fare_sex_class = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
# 打印结果
print(f"每种性别和客舱等级组合的平均票价是 {mean_fare_sex_class}")
```
