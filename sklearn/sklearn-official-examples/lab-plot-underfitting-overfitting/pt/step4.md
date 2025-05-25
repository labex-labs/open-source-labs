# Ajustar Modelos com Recursos Polinomiais

Vamos ajustar modelos com recursos polinomiais de grau 1, 4 e 15, e plotar os resultados.

```python
degrees = [1, 4, 15]

plt.figure(figsize=(14, 5))

for i in range(len(degrees)):
    ax = plt.subplot(1, len(degrees), i + 1)
    plt.setp(ax, xticks=(), yticks=())

    polynomial_features = PolynomialFeatures(degree=degrees[i], include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression),
        ]
    )
    pipeline.fit(X[:, np.newaxis], y)

    X_test = np.linspace(0, 1, 100)
    plt.plot(X_test, pipeline.predict(X_test[:, np.newaxis]), label="Modelo")
    plt.plot(X_test, true_fun(X_test), label="Função verdadeira")
    plt.scatter(X, y, edgecolor="b", s=20, label="Amostras")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim((0, 1))
    plt.ylim((-2, 2))
    plt.legend(loc="best")
    plt.title("Grau {}".format(degrees[i]))

plt.show()
```
