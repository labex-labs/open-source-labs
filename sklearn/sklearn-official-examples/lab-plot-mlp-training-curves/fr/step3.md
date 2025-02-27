# Définissez une fonction pour tracer les courbes d'apprentissage

Ensuite, nous devons définir une fonction qui tracera les courbes d'apprentissage pour chaque stratégie d'apprentissage sur chaque ensemble de données. La fonction prend en entrée l'ensemble de données (X, y), un axe sur lequel tracer et un nom pour l'ensemble de données. Nous utiliserons MinMaxScaler pour mettre à l'échelle les données et MLPClassifier pour entraîner le réseau de neurones. Nous entraînerons le réseau en utilisant chaque stratégie d'apprentissage, en ignorant les avertissements de convergence, et tracerons les courbes d'apprentissage pour chaque stratégie sur le même graphique.

```python
def plot_on_dataset(X, y, ax, name):
    # pour chaque ensemble de données, trace l'apprentissage pour chaque stratégie d'apprentissage
    print("\napprentissage sur l'ensemble de données %s" % name)
    ax.set_title(name)

    X = MinMaxScaler().fit_transform(X)
    mlps = []
    if name == "digits":
        # digits est plus grand mais converge assez rapidement
        max_iter = 15
    else:
        max_iter = 400

    for label, param in zip(labels, params):
        print("entraînement: %s" % label)
        mlp = MLPClassifier(random_state=0, max_iter=max_iter, **param)

        # certaines combinaisons de paramètres ne convergeront pas comme on peut le voir sur les
        # graphiques, donc elles sont ignorées ici
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore", category=ConvergenceWarning, module="sklearn"
            )
            mlp.fit(X, y)

        mlps.append(mlp)
        print("Score de l'ensemble d'entraînement: %f" % mlp.score(X, y))
        print("Perte de l'ensemble d'entraînement: %f" % mlp.loss_)
    for mlp, label, args in zip(mlps, labels, plot_args):
        ax.plot(mlp.loss_curve_, label=label, **args)
```
