# Representar os Resultados

Agora, representaremos os resultados para cada uma das diferentes situações.

```python
for title, this_X, this_y in [
    ("Apenas Erros de Modelação", X, y),
    ("X Corrompido, Pequenos Desvios", X_errors, y),
    ("y Corrompido, Pequenos Desvios", X, y_errors),
    ("X Corrompido, Grandes Desvios", X_errors_large, y),
    ("y Corrompido, Grandes Desvios", X, y_errors_large),
]:
    plt.figure(figsize=(5, 4))
    plt.plot(this_X[:, 0], this_y, "b+")

    for name, estimator in estimators:
        model = make_pipeline(PolynomialFeatures(3), estimator)
        model.fit(this_X, this_y)
        mse = mean_squared_error(model.predict(X_test), y_test)
        y_plot = model.predict(x_plot[:, np.newaxis])
        plt.plot(
            x_plot,
            y_plot,
            color=colors[name],
            linestyle=linestyle[name],
            linewidth=lw,
            label="%s: erro = %.3f" % (name, mse),
        )

    legend_title = "Erro de Desvio Médio\nAbsoluto em relação aos Dados Não Corrompidos"
    legend = plt.legend(
        loc="upper right", frameon=False, title=legend_title, prop=dict(size="x-small")
    )
    plt.xlim(-4, 10.2)
    plt.ylim(-2, 10.2)
    plt.title(title)
plt.show()
```
