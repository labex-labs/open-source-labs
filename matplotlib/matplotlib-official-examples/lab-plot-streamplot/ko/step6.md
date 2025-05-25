# 시작점 제어

이 단계에서는 시작점을 제어하는 streamplot 을 생성합니다. `start_points` 매개변수는 streamline 의 시작점을 나타내는 2D 배열을 사용합니다.

```python
seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1, 0, 1, 2, 2]])

strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2,
                      cmap='autumn', start_points=seed_points.T)
plt.colorbar(strm.lines)
plt.title('Controlling Starting Points')
plt.plot(seed_points[0], seed_points[1], 'bo')
plt.xlim(-w, w)
plt.ylim(-w, w)
plt.show()
```
