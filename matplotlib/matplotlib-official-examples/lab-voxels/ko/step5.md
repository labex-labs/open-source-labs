# 복셀 배열 플롯

마지막으로, `Axes3D.voxels` 함수를 사용하여 지정된 색상으로 복셀 배열을 플롯할 수 있습니다.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
