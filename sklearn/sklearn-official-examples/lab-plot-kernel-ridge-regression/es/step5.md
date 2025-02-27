# Visualizar los tiempos de entrenamiento y predicción

Visualizaremos el tiempo de ajuste y predicción de KRR y SVR para diferentes tamaños del conjunto de entrenamiento.

```python
_, ax = plt.subplots()

sizes = np.logspace(1, 3.8, 7).astype(int)
for name, estimator in {
    "KRR": KernelRidge(kernel="rbf", alpha=0.01, gamma=10),
    "SVR": SVR(kernel="rbf", C=1e2, gamma=10),
}.items():
    train_time = []
    test_time = []
    for train_test_size in sizes:
        t0 = time.time()
        estimator.fit(X[:train_test_size], y[:train_test_size])
        train_time.append(time.time() - t0)

        t0 = time.time()
        estimator.predict(X_plot[:1000])
        test_time.append(time.time() - t0)

    plt.plot(
        sizes,
        train_time,
        "o-",
        color="r" if name == "SVR" else "g",
        label="%s (entrenamiento)" % name,
    )
    plt.plot(
        sizes,
        test_time,
        "o--",
        color="r" if name == "SVR" else "g",
        label="%s (prueba)" % name,
    )

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Tamaño del entrenamiento")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de ejecución")
_ = plt.legend(loc="best")
```
