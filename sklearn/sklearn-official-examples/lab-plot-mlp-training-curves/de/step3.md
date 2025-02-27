# Definieren einer Funktion zum Zeichnen der Lernkurven

Als nächstes müssen wir eine Funktion definieren, die die Lernkurven für jede Lernstrategie auf jedem Datensatz zeichnet. Die Funktion erhält den Datensatz (X, y), eine Achse zum Zeichnen und einen Namen für den Datensatz. Wir werden MinMaxScaler verwenden, um die Daten zu skalieren, und MLPClassifier, um das neuronale Netz zu trainieren. Wir werden das Netz mit jeder Lernstrategie trainieren, Konvergenzwarnungen ignorieren und die Lernkurven für jede Strategie auf derselben Grafik zeichnen.

```python
def plot_on_dataset(X, y, ax, name):
    # für jeden Datensatz zeichnen wir das Lernen für jede Lernstrategie
    print("\nLernen auf Datensatz %s" % name)
    ax.set_title(name)

    X = MinMaxScaler().fit_transform(X)
    mlps = []
    if name == "digits":
        # digits ist größer, konvergiert aber recht schnell
        max_iter = 15
    else:
        max_iter = 400

    for label, param in zip(labels, params):
        print("Training: %s" % label)
        mlp = MLPClassifier(random_state=0, max_iter=max_iter, **param)

        # einige Parameterkombinationen werden nicht konvergieren, wie man auf den
        # Grafiken sehen kann, daher werden sie hier ignoriert
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore", category=ConvergenceWarning, module="sklearn"
            )
            mlp.fit(X, y)

        mlps.append(mlp)
        print("Training set score: %f" % mlp.score(X, y))
        print("Training set loss: %f" % mlp.loss_)
    for mlp, label, args in zip(mlps, labels, plot_args):
        ax.plot(mlp.loss_curve_, label=label, **args)
```