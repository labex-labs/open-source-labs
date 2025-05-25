# PCA 결과 시각화

PCA 결과를 시각화하여 주요 구성 요소를 플롯합니다. 데이터의 3 차원 산점도를 생성하고 각 점을 밀도에 따라 색상으로 표시합니다. 그런 다음 첫 번째 두 개의 주요 구성 요소를 평면으로 플롯합니다. 데이터의 두 가지 다른 보기에 대해 이 프로세스를 반복합니다.

```python
fig = plt.figure(figsize=(10, 5))

# 첫 번째 보기
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("View 1")

# 데이터 플롯
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# 주요 구성 요소 플롯
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# 두 번째 보기
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("View 2")

# 데이터 플롯
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# 주요 구성 요소 플롯
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
