# Регистрация конвертера с локализацией

Мы также можем зарегистрировать конвертер с локализацией, передав именованные аргументы в `~.dates.ConciseDateConverter` и зарегистрировав типы данных, которые вы будете использовать, в реестре единиц измерения.

```python
import datetime

formats = ['%y',          # метки делений в основном годы
           '%b',     # метки делений в основном месяцы
           '%d',     # метки делений в основном дни
           '%H:%M',  # часы
           '%H:%M',  # минуты
           '%S.%f', ]  # секунды
# эти могут быть такими же, за исключением смещения на один уровень....
zero_formats = [''] + formats[:-1]
#...за исключением меток делений, которые в основном часы, тогда приятно иметь день-месяц
zero_formats[3] = '%d-%b'
offset_formats = ['',
                  '%Y',
                  '%b %Y',
                  '%d %b %Y',
                  '%d %b %Y',
                  '%d %b %Y %H:%M', ]

converter = mdates.ConciseDateConverter(
    formats=formats, zero_formats=zero_formats, offset_formats=offset_formats)

munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter registered non-default')
plt.show()
```
