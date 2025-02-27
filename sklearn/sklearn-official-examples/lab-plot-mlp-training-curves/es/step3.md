# Definir una función para trazar las curvas de aprendizaje

A continuación, necesitamos definir una función que trazará las curvas de aprendizaje para cada estrategia de aprendizaje en cada conjunto de datos. La función recibe el conjunto de datos (X, y), un eje para trazar y un nombre para el conjunto de datos. Usaremos MinMaxScaler para escalar los datos y MLPClassifier para entrenar la red neuronal. Entrenaremos la red usando cada estrategia de aprendizaje, ignorando las advertencias de convergencia, y trazaremos las curvas de aprendizaje para cada estrategia en la misma gráfica.

```python
def plot_on_dataset(X, y, ax, name):
    # para cada conjunto de datos, trazar el aprendizaje para cada estrategia de aprendizaje
    print("\naprendiendo en el conjunto de datos %s" % name)
    ax.set_title(name)

    X = MinMaxScaler().fit_transform(X)
    mlps = []
    if name == "digits":
        # digits es más grande pero converge bastante rápidamente
        max_iter = 15
    else:
        max_iter = 400

    for label, param in zip(labels, params):
        print("entrenando: %s" % label)
        mlp = MLPClassifier(random_state=0, max_iter=max_iter, **param)

        # algunas combinaciones de parámetros no convergerán como se puede ver en
        # las gráficas, por lo que se ignoran aquí
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore", category=ConvergenceWarning, module="sklearn"
            )
            mlp.fit(X, y)

        mlps.append(mlp)
        print("Puntuación del conjunto de entrenamiento: %f" % mlp.score(X, y))
        print("Pérdida del conjunto de entrenamiento: %f" % mlp.loss_)
    for mlp, label, args in zip(mlps, labels, plot_args):
        ax.plot(mlp.loss_curve_, label=label, **args)
```
