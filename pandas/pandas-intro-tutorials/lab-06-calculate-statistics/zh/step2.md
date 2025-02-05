# 计算汇总统计信息

在这一步中，我们将计算泰坦尼克号数据集的汇总统计信息。

```python
# 计算泰坦尼克号乘客的平均年龄
average_age = titanic["Age"].mean()
# 打印结果
print(f"泰坦尼克号乘客的平均年龄是 {average_age}")

# 计算泰坦尼克号乘客的年龄中位数和票价中位数
median_age_fare = titanic[["Age", "Fare"]].median()
# 打印结果
print(f"泰坦尼克号乘客的年龄中位数和票价中位数是 {median_age_fare}")
```
