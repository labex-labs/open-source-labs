# 对表格行进行排序

按照乘客年龄对泰坦尼克号数据集进行排序，然后再按客舱等级和年龄以降序排列。

```python
# 按年龄排序
titanic.sort_values(by="Age").head()

# 按客舱等级和年龄以降序排序
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```
