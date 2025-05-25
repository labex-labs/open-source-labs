# 플롯의 제한 설정

`set` 메서드를 사용하여 플롯의 제한을 설정하고 X, Y, Z 좌표의 제한을 전달합니다.

```python
# Set limits of the plot from coord limits
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])
```
