# 결과 시각화

마지막으로 matplotlib 를 사용하여 결과를 시각화합니다. 데이터 포인트의 실제 위치, MDS 를 사용한 데이터 포인트의 위치, 비메트릭 MDS 를 사용한 데이터 포인트의 위치를 플롯합니다. 또한 matplotlib 의 LineCollection 을 사용하여 데이터 포인트 간의 쌍대 거리를 플롯합니다.

```python
fig = plt.figure(1)
ax = plt.axes([0.0, 0.0, 1.0, 1.0])

s = 100
plt.scatter(X_true[:, 0], X_true[:, 1], color="navy", s=s, lw=0, label="True Position")
plt.scatter(pos[:, 0], pos[:, 1], color="turquoise", s=s, lw=0, label="MDS")
plt.scatter(npos[:, 0], npos[:, 1], color="darkorange", s=s, lw=0, label="NMDS")
plt.legend(scatterpoints=1, loc="best", shadow=False)

similarities = similarities.max() / (similarities + EPSILON) * 100
np.fill_diagonal(similarities, 0)
# 에지 플롯
start_idx, end_idx = np.where(pos)
# (*line0*, *line1*, *line2*) 의 시퀀스, 여기서::
#            linen = (x0, y0), (x1, y1), ... (xm, ym)
segments = [
    [X_true[i, :], X_true[j, :]] for i in range(len(pos)) for j in range(len(pos))
]
values = np.abs(similarities)
lc = LineCollection(
    segments, zorder=0, cmap=plt.cm.Blues, norm=plt.Normalize(0, values.max())
)
lc.set_array(similarities.flatten())
lc.set_linewidths(np.full(len(segments), 0.5))
ax.add_collection(lc)

plt.show()
```
