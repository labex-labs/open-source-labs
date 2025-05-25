# Visualizar Tempos de Treinamento e Predição

Vamos visualizar o tempo de ajuste e previsão do KRR e do SVR para diferentes tamanhos do conjunto de treinamento.

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
        label="%s (treinamento)" % name,
    )
    plt.plot(
        sizes,
        test_time,
        "o--",
        color="r" if name == "SVR" else "g",
        label="%s (teste)" % name,
    )

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Tamanho do conjunto de treinamento")
plt.ylabel("Tempo (segundos)")
plt.title("Tempo de Execução")
_ = plt.legend(loc="best")
```
