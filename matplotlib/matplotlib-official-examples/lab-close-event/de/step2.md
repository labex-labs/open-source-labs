# Erstellen einer Figur und Verknüpfen des Schließereignisses

In diesem Schritt erstellen wir eine Figur und verbinden das Schließereignis mit der in Schritt 1 definierten `on_close`-Funktion. Dies wird mit der `mpl_connect`-Methode der Zeichenfläche der Figur durchgeführt.

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```
