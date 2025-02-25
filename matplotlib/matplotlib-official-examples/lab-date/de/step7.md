# Tick-Labels manuell formatieren

Wir werden die Tick-Labels auf dem dritten Subplot manuell formatieren, indem wir `DateFormatter` verwenden, um die Daten mit den im Dokumentation von `datetime.date.strftime` beschriebenen Formatzeichenfolgen zu formatieren.

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```
