# 구조적 계층적 군집 시각화

`matplotlib` 라이브러리를 사용하여 구조적 계층적 군집을 시각화합니다.

```python
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection="3d", elev=7, azim=-80)
for l in np.unique(label):
    ax2.scatter(
        X[label == l, 0],
        X[label == l, 1],
        X[label == l, 2],
        color=plt.cm.jet(float(l) / np.max(label + 1)),
        s=20,
        edgecolor="k",
    )
```
