# B スプライン補間

B スプライン基底関数を生成し、訓練データに対してリッジ回帰モデルを適合させるために `SplineTransformer` を使用します。そして、関数、訓練点、および B スプラインを使った補間を描画します。

```python
# B-spline with 4 + 3 - 1 = 6 basis functions
model = make_pipeline(SplineTransformer(n_knots=4, degree=3), Ridge(alpha=1e-3))
model.fit(X_train, y_train)

y_plot = model.predict(X_plot)
ax.plot(x_plot, y_plot, label="B-spline")
ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
