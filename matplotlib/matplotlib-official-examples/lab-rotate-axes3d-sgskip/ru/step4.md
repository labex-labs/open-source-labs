# Вращение осей и обновление диаграммы

Наконец, мы будем вращать оси и обновлять диаграмму с использованием цикла for, который проходит полный оборот по углам наклона, азимута, крена и всех вместе. Мы будем использовать функцию `ax.view_init()` для обновления вида осей и заголовка, а функции `plt.title()`, `plt.draw()` и `plt.pause()` для отображения анимации.

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
