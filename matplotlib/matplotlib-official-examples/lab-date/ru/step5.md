# Форматируем метки делений с использованием стандартного форматтера

Мы будем форматировать метки делений на первом подграфике с использованием стандартного форматтера.

```python
ax = axs[0]
ax.set_title('DefaultFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
```
