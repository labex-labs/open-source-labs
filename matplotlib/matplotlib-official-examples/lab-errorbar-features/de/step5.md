# Variable, asymmetrische Fehlerbalken plotten

Als nächstes werden wir unsere Daten mit variablen, asymmetrischen Fehlerbalken plotten. Die Funktion `ax.errorbar()` wird erneut verwendet, aber diesmal wird der Parameter `xerr` verwendet, um die asymmetrischen Fehlerwerte anzugeben.

```python
# plot variable, asymmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
