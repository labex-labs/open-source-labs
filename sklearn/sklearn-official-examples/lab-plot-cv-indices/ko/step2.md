# 교차 검증 지표 시각화

이 단계에서는 각 교차 검증 객체의 동작을 시각화하는 함수를 정의합니다. 데이터를 4 개의 분할로 나눕니다. 각 분할에서 학습 세트 (파란색) 와 테스트 세트 (빨간색) 에 선택된 인덱스를 시각화합니다.

```python
def plot_cv_indices(cv, X, y, group, ax, n_splits, lw=10):
    """교차 검증 객체의 인덱스에 대한 샘플 플롯을 만듭니다."""

    # 각 CV 분할에 대한 학습/테스트 시각화 생성
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # 학습/테스트 그룹으로 인덱스 채우기
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # 결과 시각화
        ax.scatter(
            range(len(indices)),
            [ii + 0.5] * len(indices),
            c=indices,
            marker="_",
            lw=lw,
            cmap=cmap_cv,
            vmin=-0.2,
            vmax=1.2,
        )

    # 마지막에 데이터 클래스와 그룹 플롯
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # 서식 지정
    yticklabels = list(range(n_splits)) + ["class", "group"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="샘플 인덱스",
        ylabel="CV 반복",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```
