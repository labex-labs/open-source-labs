# Graficar las curvas reales y predichas con verosimilitud marginal logarítmica (L)

Graficamos las curvas reales y predichas con la verosimilitud marginal logarítmica (L).

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
for i, ax in enumerate(axes):
    # Bayesian ridge regression with different initial value pairs
    if i == 0:
        init = [1 / np.var(y_train), 1.0]  # Valores predeterminados
    elif i == 1:
        init = [1.0, 1e-3]
        reg.set_params(alpha_init=init[0], lambda_init=init[1])
    reg.fit(X_train, y_train)
    ymean, ystd = reg.predict(X_test, return_std=True)

    ax.plot(x_test, func(x_test), color="blue", label="sin($2\\pi x$)")
    ax.scatter(x_train, y_train, s=50, alpha=0.5, label="observación")
    ax.plot(x_test, ymean, color="red", label="predicción media")
    ax.fill_between(
        x_test, ymean - ystd, ymean + ystd, color="pink", alpha=0.5, label="predicción std"
    )
    ax.set_ylim(-1.3, 1.3)
    ax.legend()
    título = "$\\alpha$_init$={:.2f},\\ \\lambda$_init$={}$".format(init[0], init[1])
    if i == 0:
        título += " (Predeterminado)"
    ax.set_title(título, fontsize=12)
    texto = "$\\alpha={:.1f}$\n$\\lambda={:.3f}$\n$L={:.1f}$".format(
        reg.alpha_, reg.lambda_, reg.scores_[-1]
    )
    ax.text(0.05, -1.0, texto, fontsize=12)

plt.tight_layout()
plt.show()
```
