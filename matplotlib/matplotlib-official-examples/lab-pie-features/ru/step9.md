# Изменение тени

Мы можем изменить тень круговой диаграммы, передав словарь аргументов в параметр `shadow` функции `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none','shade': 0.9}, startangle=90)
```
