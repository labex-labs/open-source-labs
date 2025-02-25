# Управление размером

Мы можем управлять размером круговой диаграммы, устанавливая параметр `radius` функции `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size':'smaller'}, radius=0.5)
```
