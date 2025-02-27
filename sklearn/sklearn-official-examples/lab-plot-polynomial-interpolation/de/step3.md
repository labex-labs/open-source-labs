# B-Spline-Interpolation

Wir werden `SplineTransformer` verwenden, um B-Spline-Basisfunktionen zu generieren und ein Ridge-Regressionsmodell an die Trainingsdaten anzupassen. Anschließend plotten wir die Funktion, die Trainingspunkte und die Interpolation mit B-Splines.

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
