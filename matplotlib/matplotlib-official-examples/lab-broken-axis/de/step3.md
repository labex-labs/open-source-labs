# Erstellen der Teilplots (Subplots)

Als Nächstes werden wir zwei Teilplots erstellen: einen für die Ausreißer und einen für die Mehrheit der Daten. Wir verwenden `plt.subplots`, um die Teilplots zu erstellen und setzen den Parameter `sharex` auf `True`, damit sie die gleiche x-Achse verwenden.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
```
