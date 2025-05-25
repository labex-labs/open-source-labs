# 복셀 플롯 (Voxel Plot) 그리기

마지막으로, `ax.voxels` 함수를 사용하여 복셀 플롯을 그릴 수 있습니다. RGB 값, 구에 대한 조건, 면 색상, 가장자리 색상 및 선 너비를 전달합니다.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```
