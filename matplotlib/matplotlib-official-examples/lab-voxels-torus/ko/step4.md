# 3D 복셀 플롯 생성

이제 `ax.voxels` 함수를 사용하여 3D 복셀 플롯을 생성합니다. `x`, `y`, `z`, 그리고 `sphere`를 매개변수로 전달합니다. 또한, 앞서 정의한 `colors` 배열을 사용하여 `facecolors`와 `edgecolors`를 추가합니다.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
```
