# Flaches Shading

Die `pcolormesh`-Funktion in Matplotlib kann 2D-Gitter visualisieren. Die Gitterangabe mit den wenigsten Annahmen ist `shading='flat'` und wenn das Gitter in jeder Dimension um eins größer als die Daten ist, d.h. die Form `(M+1, N+1)` hat. In diesem Fall geben `X` und `Y` die Ecken der Vierecke an, die mit den Werten in `Z` gefärbt werden. Wir können das Gitter mit dem folgenden Codeblock visualisieren:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='flat', cmap='viridis')
ax.set_title('Flat Shading')
plt.show()
```
