# Erstellen eines einfachen Fehlerbalkendiagramms

Wir werden ein einfaches Fehlerbalkendiagramm mit Standard-Fehlerbalken mithilfe der `errorbar`-Funktion erstellen. Hier werden wir die x- und y-Werte zusammen mit ihren entsprechenden Fehlerwerten festlegen. Wir werden auch den Linienstil auf gestrichelt setzen.

```python
fig, ax = plt.subplots(figsize=(7, 4))

# standard error bars
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```
