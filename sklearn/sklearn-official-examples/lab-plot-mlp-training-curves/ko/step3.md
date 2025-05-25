# 학습 곡선을 그리는 함수 정의

다음으로, 각 데이터셋에 대해 각 학습 전략의 학습 곡선을 그리는 함수를 정의해야 합니다. 이 함수는 데이터셋 (X, y), 플롯할 축, 데이터셋 이름을 입력으로 받습니다. 데이터를 스케일링하기 위해 MinMaxScaler 를 사용하고, 신경망을 학습시키기 위해 MLPClassifier 를 사용합니다. 각 학습 전략을 사용하여 네트워크를 학습시키고, 수렴 경고를 무시하고, 동일한 플롯에 각 전략의 학습 곡선을 그립니다.

```python
def plot_on_dataset(X, y, ax, name):
    # 각 데이터셋에 대해, 각 학습 전략의 학습을 플롯합니다.
    print("\n데이터셋 %s에서 학습" % name)
    ax.set_title(name)

    X = MinMaxScaler().fit_transform(X)
    mlps = []
    if name == "digits":
        # digits 는 크기가 크지만 상당히 빠르게 수렴합니다.
        max_iter = 15
    else:
        max_iter = 400

    for label, param in zip(labels, params):
        print("학습: %s" % label)
        mlp = MLPClassifier(random_state=0, max_iter=max_iter, **param)

        # 일부 매개변수 조합은 플롯에서 볼 수 있듯이 수렴하지 않으므로 여기서 무시됩니다.
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore", category=ConvergenceWarning, module="sklearn"
            )
            mlp.fit(X, y)

        mlps.append(mlp)
        print("학습 세트 점수: %f" % mlp.score(X, y))
        print("학습 세트 손실: %f" % mlp.loss_)
    for mlp, label, args in zip(mlps, labels, plot_args):
        ax.plot(mlp.loss_curve_, label=label, **args)
```
