# 레이블 및 Zticks 설정

`set` 메서드를 사용하여 레이블과 zticks 를 설정합니다. X, Y, Z 좌표에 대한 레이블을 설정하고, 상자의 깊이를 표시하도록 zticks 를 설정합니다.

```python
# Set labels and zticks
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```
