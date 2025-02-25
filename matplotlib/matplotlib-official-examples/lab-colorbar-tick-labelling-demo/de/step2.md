# Erstellen eines Diagramms mit einer vertikalen Farbskala

Wir beginnen mit der Erstellung eines Diagramms mit einer vertikalen Farbskala. Wir werden einige zufällige Daten mit `randn` aus `numpy` generieren und die Werte auf den Bereich von -1 bis 1 einschränken. Anschließend werden wir ein `AxesImage`-Objekt mit `imshow` und der Farbskala `coolwarm` erstellen. Schließlich werden wir einem Titel zum Diagramm hinzufügen.

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
