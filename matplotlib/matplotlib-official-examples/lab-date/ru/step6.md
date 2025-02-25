# Форматируем метки делений с использованием компактного форматтера

Мы будем форматировать метки делений на втором подграфике с использованием компактного форматтера.

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```
