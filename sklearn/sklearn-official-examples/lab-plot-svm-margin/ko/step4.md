# 여백 계산

분리 초평면의 여백을 계산합니다. 먼저 모델의 계수를 사용하여 여백 거리를 계산합니다. 그런 다음 초평면의 기울기를 사용하여 지지 벡터에서 초평면까지의 수직 거리를 계산합니다. 마지막으로 직선, 점, 그리고 평면에 가장 가까운 벡터를 플롯합니다.

```python
margin = 1 / np.sqrt(np.sum(clf.coef_**2))
yy_down = yy - np.sqrt(1 + a**2) * margin
yy_up = yy + np.sqrt(1 + a**2) * margin

plt.plot(xx, yy, "k-")
plt.plot(xx, yy_down, "k--")
plt.plot(xx, yy_up, "k--")

plt.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=80,
    facecolors="none",
    zorder=10,
    edgecolors="k",
    cmap=plt.get_cmap("RdBu"),
)
plt.scatter(
    X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.get_cmap("RdBu"), edgecolors="k"
)

plt.axis("tight")
x_min = -4.8
x_max = 4.2
y_min = -6
y_max = 6
```
