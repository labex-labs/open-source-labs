# Разделение секций

Мы можем разделить одну или несколько секций круговой диаграммы, передав список значений в параметр `explode` функции `pie()`.

```python
explode = (0, 0.1, 0, 0)  # только "разделяем" вторую секцию (то есть 'Hogs')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```
