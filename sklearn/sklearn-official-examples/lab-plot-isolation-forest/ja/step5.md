# パス長決定境界を描画する

`response_method="decision_function"` を設定することで、`DecisionBoundaryDisplay` の背景は、観測値の正規性の尺度を表します。このようなスコアは、ランダムな木の森全体で平均化されたパス長によって与えられ、それ自体は、特定のサンプルを分離するために必要な葉の深さ（または同じことである分割数）によって与えられます。

```python
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="decision_function",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("Path length decision boundary \nof IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["outliers", "inliers"], title="true class")
plt.colorbar(disp.ax_.collections[1])
plt.show()
```
