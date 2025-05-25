# 3D 등고선 플롯 생성

생성된 삼각화와 z 좌표를 사용하여 3D 등고선 플롯을 생성합니다. 또한 플롯을 더 쉽게 이해할 수 있도록 뷰 각도를 사용자 정의합니다.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```
