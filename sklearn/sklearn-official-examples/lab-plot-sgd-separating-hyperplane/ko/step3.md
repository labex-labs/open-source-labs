# 최대 마진 분류 초평면 플롯

마지막으로, SGD 를 사용한 SVM 알고리즘으로 얻은 최대 마진 분류 초평면을 플롯할 수 있습니다. `np.meshgrid`를 사용하여 점 그리드를 생성한 다음, SVM 모델의 `decision_function` 메서드를 사용하여 그리드의 각 점에 대한 결정 함수를 계산합니다. 그런 다음 `plt.contour`를 사용하여 결정 경계를 플롯하고 `plt.scatter`를 사용하여 데이터 점을 플롯합니다.

```python
# 선, 점 및 평면에 가장 가까운 벡터를 플롯합니다.
xx = np.linspace(-1, 5, 10)
yy = np.linspace(-1, 5, 10)

X1, X2 = np.meshgrid(xx, yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function([[x1, x2]])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ["dashed", "solid", "dashed"]
colors = "k"
plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolor="black", s=20)

plt.axis("tight")
plt.show()
```
