# Erstellen eines Plots mit logarithmischer Skala

Die nächste Art von Skalierungsumformung, die wir untersuchen werden, ist die logarithmische Skala. Um einen Plot mit logarithmischer Skala zu erstellen, verwenden wir die Methode `set_yscale()` und übergeben den String `'log'`. Wir fügen auch einen Titel und ein Gitter zum Plot hinzu.

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.grid(True)
```
