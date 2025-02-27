# 学習曲線をプロットする関数を定義する

次に、各データセットに対して各学習戦略の学習曲線をプロットする関数を定義する必要があります。この関数は、データセット (X, y)、プロットする軸、およびデータセットの名前を引数として受け取ります。MinMaxScaler を使用してデータをスケーリングし、MLPClassifier を使用してニューラルネットワークを訓練します。各学習戦略を使用してネットワークを訓練し、収束警告を無視して、同じグラフに各戦略の学習曲線をプロットします。

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
