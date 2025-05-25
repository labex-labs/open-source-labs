# Formatar os rótulos de marcação manualmente

Formataremos os rótulos de marcação no terceiro subplot manualmente usando `DateFormatter` para formatar as datas usando as strings de formato documentadas em `datetime.date.strftime`.

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```
