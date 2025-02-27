# 決定境界と学習ポイントを描画する

このステップでは、決定境界と学習ポイントを描画します。`sklearn.inspection`モジュールの`from_estimator`メソッドを使って`DecisionBoundaryDisplay`オブジェクトを作成し、AdaBoost分類器、データセット、その他のパラメータを渡します。また、各クラスに異なる色を使って学習ポイントを描画します。

```python
plot_colors = "br"
plot_step = 0.02
class_names = "AB"

plt.figure(figsize=(10, 5))

# 決定境界を描画する
ax = plt.subplot(121)
disp = DecisionBoundaryDisplay.from_estimator(
    bdt,
    X,
    cmap=plt.cm.Paired,
    response_method="predict",
    ax=ax,
    xlabel="x",
    ylabel="y",
)
x_min, x_max = disp.xx0.min(), disp.xx0.max()
y_min, y_max = disp.xx1.min(), disp.xx1.max()
plt.axis("tight")

# 学習ポイントを描画する
for i, n, c in zip(range(2), class_names, plot_colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=c,
        cmap=plt.cm.Paired,
        s=20,
        edgecolor="k",
        label="Class %s" % n,
    )
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc="upper right")

plt.title("Decision Boundary")
```
