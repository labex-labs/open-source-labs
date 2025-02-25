# Локализация форматов дат

Форматы дат можно локализовать, если стандартные форматы не подходят, путём манипуляции с одним из трёх списков строк. Мы модифицируем метки, чтобы они были в формате "день месяц год", а не в ISO формате "год месяц день".

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))

for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    formatter.formats = ['%y',  # метки делений в основном годы
                         '%b',       # метки делений в основном месяцы
                         '%d',       # метки делений в основном дни
                         '%H:%M',    # часы
                         '%H:%M',    # минуты
                         '%S.%f', ]  # секунды
    # эти в основном просто предыдущий уровень...
    formatter.zero_formats = [''] + formatter.formats[:-1]
    #...за исключением меток делений, которые в основном часы, тогда лучше иметь
    # день-месяц:
    formatter.zero_formats[3] = '%d-%b'

    formatter.offset_formats = ['',
                                '%Y',
                                '%b %Y',
                                '%d %b %Y',
                                '%d %b %Y',
                                '%d %b %Y %H:%M', ]
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter')
plt.show()
```
