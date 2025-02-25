# Erstellen eines Plots mit Logit-Skala

Die vierte Art von Skalierungsumformung, die wir untersuchen werden, ist die Logit-Skala. Diese Skalierung ist nützlich, wenn es um Daten geht, die zwischen 0 und 1 begrenzt sind. Um einen Plot mit Logit-Skala zu erstellen, verwenden wir die Methode `set_yscale()` und übergeben den String `'logit'`. Wir fügen auch einen Titel und ein Gitter zum Plot hinzu.

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit Scale')
plt.grid(True)
```
