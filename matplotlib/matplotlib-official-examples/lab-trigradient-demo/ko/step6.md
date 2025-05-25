# 삼각 측량, 전위 등고선 및 벡터 필드 플롯

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.use_sticky_edges = False
ax.margins(0.07)

ax.triplot(triang, color='0.8')

levels = np.arange(0., 1., 0.01)
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='hot',
              linewidths=[2.0, 1.0, 1.0, 1.0])

ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
          units='xy', scale=10., zorder=3, color='blue',
          width=0.007, headwidth=3., headlength=4.)

ax.set_title('Gradient Plot: Electrical Dipole')
plt.show()
```

설명:

- `fig`와 `ax`는 각각 figure 객체와 axes 객체입니다.
- `ax.set_aspect`는 축의 종횡비를 설정합니다.
- `ax.use_sticky_edges`와 `ax.margins`는 축의 여백을 설정합니다.
- `ax.triplot`은 삼각 측량을 플롯합니다.
- `ax.tricontour`는 전위 등고선을 플롯합니다.
- `ax.quiver`는 벡터 필드를 플롯합니다.
- `ax.set_title`은 플롯의 제목을 설정합니다.
