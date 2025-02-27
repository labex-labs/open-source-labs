# Definieren einer Funktion zum Plotten der Lernkurven

Als nächstes müssen wir eine Funktion definieren, die die Lernkurven für jede Lernstrategie auf jedem Datensatz plottet. Die Funktion nimmt den Datensatz (X, y), eine Achse zum Plotten und einen Namen für den Datensatz entgegen. Wir werden MinMaxScaler verwenden, um die Daten zu skalieren, und MLPClassifier, um das neuronale Netzwerk zu trainieren. Wir werden das Netzwerk mit jeder Lernstrategie trainieren, Konvergenzwarnungen ignorieren und die Lernkurven für jede Strategie in demselben Diagramm plotten.

```python
def plot_on_dataset(X, y, ax, name):
    # for each dataset, plot learning for each learning strategy
    print("\nlearning on dataset %s" % name)
    ax.set_title(name)

    X = MinMaxScaler().fit_transform(X)
    mlps = []
    if name == "digits":
        # digits is larger but converges fairly quickly
        max_iter = 15
    else:
        max_iter = 400

    for label, param in zip(labels, params):
        print("training: %s" % label)
        mlp = MLPClassifier(random_state=0, max_iter=max_iter, **param)

        # some parameter combinations will not converge as can be seen on the
        # plots so they are ignored here
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
