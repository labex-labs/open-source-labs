# 축 회전 및 플롯 업데이트

마지막으로, 완전한 고도, 방위각, 롤 및 모든 회전을 순환하는 for 루프를 사용하여 축을 회전하고 플롯을 업데이트합니다. `ax.view_init()` 함수를 사용하여 축 뷰와 제목을 업데이트하고, `plt.title()`, `plt.draw()`, 및 `plt.pause()` 함수를 사용하여 애니메이션을 표시합니다.

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
