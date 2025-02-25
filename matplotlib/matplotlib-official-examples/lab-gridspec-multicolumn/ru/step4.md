# Добавляем подграфики в GridSpec

Мы можем добавить подграфики в GridSpec с помощью функции `fig.add_subplot()`. Мы можем указать расположение подграфика в сетке с использованием индексирования объекта GridSpec. Например, `gs[0, :]` задает первую строку и все столбцы.

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
