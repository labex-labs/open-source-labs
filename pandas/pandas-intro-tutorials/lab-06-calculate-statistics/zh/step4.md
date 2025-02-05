# 按类别统计记录数量

最后，我们将按类别统计记录数量。

```python
# 统计每个客舱等级的乘客数量
passengers_per_class = titanic["Pclass"].value_counts()
# 打印结果
print(f"每个客舱等级的乘客数量是 {passengers_per_class}")
```
