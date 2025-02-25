# Formater manuellement les étiquettes d'échelle

Nous allons formater manuellement les étiquettes d'échelle sur le troisième sous-graphique à l'aide de `DateFormatter` pour formater les dates à l'aide des chaînes de format documentées dans `datetime.date.strftime`.

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```
