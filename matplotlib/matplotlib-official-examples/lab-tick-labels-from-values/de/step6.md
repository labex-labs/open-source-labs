# Festlegen des Tick-Formatters und -Lokators

Wir legen den x-Achsen-Tick-Formatter auf die in Schritt 5 erstellte Formatierungsfunktion mit der `set_major_formatter()`-Methode fest. Wir legen auch den x-Achsen-Tick-Lokator auf `MaxNLocator(integer=True)` fest, um sicherzustellen, dass die Tick-Werte ganzzahlige Werte annehmen.

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```
