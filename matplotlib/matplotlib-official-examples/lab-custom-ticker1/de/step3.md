# Erzeuge das Diagramm

Jetzt können wir das Diagramm mit dem benutzerdefinierten Ticker erstellen. Wir werden einen Balkendiagramm mit Beispiel-Daten erstellen und die Skalenmarkierungen der y-Achse so einstellen, dass unsere benutzerdefinierte Ticker-Funktion verwendet wird.

```python
# Erzeuge ein Balkendiagramm mit Beispiel-Daten
fig, ax = plt.subplots()
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money)

# Setze die Skalenmarkierungen der y-Achse, um die benutzerdefinierte Ticker-Funktion zu verwenden
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))

# Zeige das Diagramm an
plt.show()
```
