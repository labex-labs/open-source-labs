# Erstellen eines Plots mit symmetrischer logarithmischer Skala

Die dritte Art von Skalierungsumformung, die wir untersuchen werden, ist die symmetrische logarithmische Skala. Diese Skalierung ist nützlich, wenn es um Daten geht, die sowohl positive als auch negative Werte enthalten. Um einen Plot mit symmetrischer logarithmischer Skala zu erstellen, verwenden wir die Methode `set_yscale()` und übergeben den String `'symlog'`. Wir setzen auch den Parameter `linthresh` auf `0,02`, um den Bereich der Werte um Null anzugeben, die linear skaliert werden sollen. Wir fügen auch einen Titel und ein Gitter zum Plot hinzu.

```python
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Symmetrical Logarithmic Scale')
plt.grid(True)
```
