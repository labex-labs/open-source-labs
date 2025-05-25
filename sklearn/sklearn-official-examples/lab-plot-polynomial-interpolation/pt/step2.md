# Interpolação com Características Polinomiais

Utilizaremos `PolynomialFeatures` para gerar características polinomiais e ajustar um modelo de regressão de ridge aos dados de treino. Em seguida, representaremos graficamente a função, os pontos de treino e a interpolação utilizando características polinomiais.

```python
# representar graficamente a função
lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(
    color=["black", "teal", "yellowgreen", "gold", "darkorange", "tomato"]
)
ax.plot(x_plot, f(x_plot), linewidth=lw, label="ground truth")

# representar graficamente os pontos de treino
ax.scatter(x_train, y_train, label="pontos de treino")

# características polinomiais
for degree in [3, 4, 5]:
    model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot = model.predict(X_plot)
    ax.plot(x_plot, y_plot, label=f"grau {degree}")

ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
