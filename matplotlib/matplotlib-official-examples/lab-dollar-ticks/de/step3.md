# Formatieren der y-Achsenbeschriftungen mit Dollarzeichen

Jetzt formatieren wir die Beschriftungen der y-Achse, um Dollarzeichen anzuzeigen. Wir werden die `StrMethodFormatter`-Klasse aus dem `matplotlib.ticker`-Modul verwenden, um die Beschriftungen zu formatieren.

```python
import matplotlib.ticker as ticker

# Format y-axis labels with dollar signs
fmt = '${x:,.2f}'
tick = ticker.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
```

Im obigen Code erstellen wir ein `StrMethodFormatter`-Objekt mit der Formatzeichenkette `'$ {x:,.2f}'`. Diese Formatzeichenkette gibt an, dass wir ein Dollarzeichen gefolgt von einem Leerzeichen und einer kommagetrennten Zahl mit zwei Dezimalstellen möchten.

Als Nächstes erstellen wir ein `Tick`-Objekt unter Verwendung des gerade erstellten `StrMethodFormatter`-Objekts. Schließlich setzen wir den Haupteinteilungsformatierer der y-Achse auf das `Tick`-Objekt.
