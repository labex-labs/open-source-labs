# PCA 수행

데이터셋의 차원을 줄이기 위해 주성분 분석 (PCA) 을 수행합니다. 데이터를 첫 세 주성분에 투영하고 3 차원으로 결과를 플롯합니다.

```python
fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=y,
    cmap=plt.cm.Set1,
    edgecolor="k",
    s=40,
)

ax.set_title("첫 세 PCA 방향")
ax.set_xlabel("첫 번째 고유 벡터")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("두 번째 고유 벡터")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("세 번째 고유 벡터")
ax.zaxis.set_ticklabels([])
```
