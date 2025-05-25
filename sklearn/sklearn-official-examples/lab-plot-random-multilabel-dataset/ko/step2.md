# 플롯 함수 정의

다음으로, 랜덤으로 생성된 다중 레이블 데이터셋을 플롯하는 함수 `plot_2d`를 정의합니다. 이 함수는 세 개의 인수 `n_labels`, `n_classes`, 그리고 `length`를 받습니다.

```python
def plot_2d(ax, n_labels=1, n_classes=3, length=50):
    X, Y, p_c, p_w_c = make_ml_clf(
        n_samples=150,
        n_features=2,
        n_classes=n_classes,
        n_labels=n_labels,
        length=length,
        allow_unlabeled=False,
        return_distributions=True,
        random_state=RANDOM_SEED,
    )

    ax.scatter(
        X[:, 0], X[:, 1], color=COLORS.take((Y * [1, 2, 4]).sum(axis=1)), marker="."
    )
    ax.scatter(
        p_w_c[0] * length,
        p_w_c[1] * length,
        marker="*",
        linewidth=0.5,
        edgecolor="black",
        s=20 + 1500 * p_c**2,
        color=COLORS.take([1, 2, 4]),
    )
    ax.set_xlabel("Feature 0 count")
    return p_c, p_w_c
```

이 함수는 지정된 매개변수로 `make_multilabel_classification` 함수를 사용하여 데이터셋을 생성합니다. 그런 다음 Matplotlib 라이브러리의 `scatter` 함수를 사용하여 데이터셋을 플롯합니다. 이 함수는 클래스 확률과 특징 확률을 반환합니다.
