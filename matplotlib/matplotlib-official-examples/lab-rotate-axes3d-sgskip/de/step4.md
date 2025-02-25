# Achsen drehen und Plot aktualisieren

Schließlich werden wir die Achsen drehen und den Plot mit einer for-Schleife aktualisieren, die einen vollen Drehungskreis von Elevation, Azimut, Rollwinkel und allen durchläuft. Wir werden die Funktion `ax.view_init()` verwenden, um die Achsenansicht und den Titel zu aktualisieren, und die Funktionen `plt.title()`, `plt.draw()` und `plt.pause()` verwenden, um die Animation anzuzeigen.

```python
# Rotate the axes and update the plot
for angle in range(0, 360*4 + 1):
    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180

    # Cycle through a full rotation of elevation, then azimuth, roll, and all
    elev = azim = roll = 0
    if angle <= 360:
        elev = angle_norm
    elif angle <= 360*2:
        azim = angle_norm
    elif angle <= 360*3:
        roll = angle_norm
    else:
        elev = azim = roll = angle_norm

    # Update the axis view and title
    ax.view_init(elev, azim, roll)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

    # Display animation
    plt.draw()
    plt.pause(.001)
```
