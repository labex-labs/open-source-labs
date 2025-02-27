# Polynomiale Merkmalsinterpolation

Wir werden `PolynomialFeatures` verwenden, um polynomiale Merkmale zu generieren und ein Ridge-Regressionsmodell an die Trainingsdaten anzupassen. Anschließend plotten wir die Funktion, die Trainingspunkte und die Interpolation mit polynomiellen Merkmalen.

```python
# plot function
lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(
    color=["black", "teal", "yellowgreen", "gold", "darkorange", "tomato"]
)
ax.plot(x_plot, f(x_plot), linewidth=lw, label="ground truth")

# plot training points
ax.scatter(x_train, y_train, label="training points")

# polynomial features
for degree in [3, 4, 5]:
    model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot = model.predict(X_plot)
    ax.plot(x_plot, y_plot, label=f"degree {degree}")

ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
