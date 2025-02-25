# Daten für das Plotten erstellen

Als nächstes müssen wir einige Daten für das Plotten erstellen. In diesem Lab werden wir die Sinusfunktion verwenden, um unsere Daten zu generieren. Wir werden 500 gleichmäßig verteilte Punkte zwischen 0 und 10 erzeugen und den Sinus jedes Punktes mithilfe der `np.sin()`-Funktion berechnen.

```python
x = np.linspace(0, 10, 500)
y = np.sin(x)
```
