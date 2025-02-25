# Erstellen eines Diagramms mit einer horizontalen Farbskala

Wir werden nun ein Diagramm mit einer horizontalen Farbskala erstellen. Wir werden die gleichen Schritte wie in Schritt 2 folgen, aber diesmal werden wir die Farbskala `afmhot` verwenden und die Ausrichtung der Farbskala horizontal setzen.

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
