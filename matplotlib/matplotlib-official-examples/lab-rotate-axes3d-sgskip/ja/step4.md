# 軸を回転させてプロットを更新する

最後に、仰角、方位角、ロールの完全な回転を繰り返す for ループを使って軸を回転させ、プロットを更新します。`ax.view_init()`関数を使って軸のビューとタイトルを更新し、`plt.title()`、`plt.draw()`、および`plt.pause()`関数を使ってアニメーションを表示します。

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
