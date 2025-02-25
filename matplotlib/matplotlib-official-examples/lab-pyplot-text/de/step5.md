# Titel, X-Beschriftung und Y-Beschriftung hinzufügen

Wir können Titel, X-Beschriftung und Y-Beschriftung zum Diagramm hinzufügen, indem wir die `title()`, `xlabel()` und `ylabel()`-Methoden der `pyplot`-Bibliothek verwenden. Wir werden "Spannung gegen Zeit" als Titel, "Zeit [s]" als X-Beschriftung und "Spannung [mV]" als Y-Beschriftung hinzufügen.

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```
