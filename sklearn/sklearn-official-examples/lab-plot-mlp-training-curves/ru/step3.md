# Определение функции для построения кривых обучения

Далее нам нужно определить функцию, которая будет строить кривые обучения для каждой стратегии обучения на каждом наборе данных. Функция принимает набор данных (X, y), ось для построения графика и название набора данных. Мы будем использовать `MinMaxScaler` для масштабирования данных и `MLPClassifier` для обучения нейронной сети. Мы обучим сеть с использованием каждой стратегии обучения, игнорируя предупреждения о неконвергенции, и построим кривые обучения для каждой стратегии на одном графике.

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
