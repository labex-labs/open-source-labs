# Настройка штриховок

Мы можем настроить штриховки секций, передав список штриховок в параметр `hatch` функции `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```
