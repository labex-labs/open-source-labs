# B-Spline Interpolation

We will use `SplineTransformer` to generate B-spline basis functions and fit a ridge regression model to the training data. Then we plot the function, training points, and the interpolation using B-splines.

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
