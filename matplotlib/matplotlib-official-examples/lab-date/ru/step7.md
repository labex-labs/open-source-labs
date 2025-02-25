# Вручную форматируем метки делений

Мы вручную отформатируем метки делений на третьем подграфике с использованием `DateFormatter` для форматирования дат с использованием строк формата, описанных в `datetime.date.strftime`.

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```
