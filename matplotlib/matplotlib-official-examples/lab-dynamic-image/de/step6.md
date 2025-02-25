# Erstelle die Animation

Wir werden jetzt die Animation mit der `ArtistAnimation`-Methode erstellen. Wir werden das Figure-Objekt, die `ims`-Liste, den Zeitintervall zwischen den Frames und die Wiederholverzögerung übergeben.

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
