# Anpassen der Achsenbeschriftungen

Wir können auch die Achsenbeschriftungen unseres Graphen mithilfe des Schriftartwörterbuchs anpassen. Wir werden den fontdict-Parameter der xlabel()- und ylabel()-Funktionen auf unser Schriftartwörterbuch setzen.

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
