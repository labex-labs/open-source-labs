# Beschriftungen und Z-Ticks festlegen

Legen Sie die Beschriftungen und Z-Ticks mit der `set`-Methode fest. Wir werden die Beschriftungen für die X-, Y- und Z-Koordinaten festlegen und die Z-Ticks so einstellen, dass die Tiefe der Box angezeigt wird.

```python
# Set labels and zticks
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```
