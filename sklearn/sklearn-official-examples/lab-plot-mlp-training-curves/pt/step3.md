# Definir uma função para plotar as curvas de aprendizagem

Em seguida, precisamos definir uma função que plotará as curvas de aprendizagem para cada estratégia de aprendizagem em cada conjunto de dados. A função recebe o conjunto de dados (X, y), um eixo para plotar e um nome para o conjunto de dados. Usaremos MinMaxScaler para escalar os dados e MLPClassifier para treinar a rede neural. Treinaremos a rede usando cada estratégia de aprendizagem, ignorando avisos de convergência, e plotaremos as curvas de aprendizagem para cada estratégia no mesmo gráfico.

```python
def plot_on_dataset(X, y, ax, name):
    # para cada conjunto de dados, plota o aprendizado para cada estratégia de aprendizagem
    print("\naprendendo no conjunto de dados %s" % name)
    ax.set_title(name)

    X = MinMaxScaler().fit_transform(X)
    mlps = []
    if name == "digits":
        # digits é maior, mas converge razoavelmente rápido
        max_iter = 15
    else:
        max_iter = 400

    for label, param in zip(labels, params):
        print("treinamento: %s" % label)
        mlp = MLPClassifier(random_state=0, max_iter=max_iter, **param)

        # algumas combinações de parâmetros não convergirão, como pode ser visto nos
        # gráficos, portanto, são ignoradas aqui
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore", category=ConvergenceWarning, module="sklearn"
            )
            mlp.fit(X, y)

        mlps.append(mlp)
        print("Pontuação do conjunto de treinamento: %f" % mlp.score(X, y))
        print("Perda do conjunto de treinamento: %f" % mlp.loss_)
    for mlp, label, args in zip(mlps, labels, plot_args):
        ax.plot(mlp.loss_curve_, label=label, **args)
```
