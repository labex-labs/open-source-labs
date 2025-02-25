# Die Animation erstellen

Schließlich werden wir die Animation mit dem `FuncAnimation`-Objekt erstellen, indem wir die Figur, die Aktualisierungsfunktion, den Intervall zwischen den Frames in Millisekunden und die Anzahl der zu speichernden Frames übergeben.

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
