# 복셀 플롯 생성

마지막으로, Matplotlib 의 `Axes3D` 클래스의 `voxels` 함수를 사용하여 3D 복셀 플롯을 생성합니다.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
