# Добавление меток к секциям

Мы можем добавить метки к секциям, передав список меток в параметр `labels` функции `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```
