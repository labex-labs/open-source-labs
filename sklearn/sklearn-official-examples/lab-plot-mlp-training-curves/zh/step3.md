# 定义一个绘制学习曲线的函数

接下来，我们需要定义一个函数，该函数将为每个数据集上的每种学习策略绘制学习曲线。该函数接受数据集（X，y）、要绘制的轴以及数据集的名称。我们将使用MinMaxScaler对数据进行缩放，并使用MLPClassifier训练神经网络。我们将使用每种学习策略训练网络，忽略收敛警告，并在同一图上为每种策略绘制学习曲线。

```python
def plot_on_dataset(X, y, ax, name):
    # 对于每个数据集，绘制每种学习策略的学习情况
    print("\n在数据集 %s 上进行学习" % name)
    ax.set_title(name)

    X = MinMaxScaler().fit_transform(X)
    mlps = []
    if name == "digits":
        # digits数据集较大，但收敛相当快
        max_iter = 15
    else:
        max_iter = 400

    for label, param in zip(labels, params):
        print("训练: %s" % label)
        mlp = MLPClassifier(random_state=0, max_iter=max_iter, **param)

        # 从图中可以看出，一些参数组合不会收敛，因此在这里被忽略
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore", category=ConvergenceWarning, module="sklearn"
            )
            mlp.fit(X, y)

        mlps.append(mlp)
        print("训练集得分: %f" % mlp.score(X, y))
        print("训练集损失: %f" % mlp.loss_)
    for mlp, label, args in zip(mlps, labels, plot_args):
        ax.plot(mlp.loss_curve_, label=label, **args)
```
