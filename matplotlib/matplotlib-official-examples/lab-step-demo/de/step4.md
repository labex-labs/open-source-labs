# Diagramm mit `.plot()` erstellen

Wir können das gleiche Verhalten wie mit `.step()` erreichen, indem wir den `drawstyle`-Parameter der `.plot()`-Funktion verwenden. Wir werden drei Diagramme mit unterschiedlichen Werten für `drawstyle` erstellen.

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

Der obige Code wird ein Diagramm mit drei stückweise konstanten Kurven erstellen, wobei jeder eine unterschiedliche `drawstyle`-Wert hat.
