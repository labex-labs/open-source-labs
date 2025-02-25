# Flaches Shading, Gitter mit derselben Form

Wenn das Gitter in jeder Dimension die gleiche Form wie die Daten hat, können wir `shading='flat'` nicht verwenden. Historisch hat Matplotlib in diesem Fall die letzte Zeile und Spalte von `Z` stillschweigend weggelassen, um dem Verhalten von Matlab zu entsprechen. Wenn dieses Verhalten immer noch gewünscht ist, lassen Sie einfach die letzte Zeile und Spalte manuell weg. Wir können das Gitter mit dem folgenden Codeblock visualisieren:

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', cmap='viridis')
ax.set_title('Flat Shading, Same Shape Grid')
plt.show()
```
