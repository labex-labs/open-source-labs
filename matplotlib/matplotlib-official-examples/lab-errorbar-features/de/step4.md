# Variable, symmetrische Fehlerbalken plotten

Wir werden jetzt unsere Daten mit variablen, symmetrischen Fehlerbalken plotten. Die Funktion `ax.errorbar()` wird verwendet, um den Plot zu erstellen, und der Parameter `yerr` wird verwendet, um die Fehlerwerte anzugeben.

```python
# plot variable, symmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
