# 교차 검증 객체 비교

이 단계에서는 scikit-learn 교차 검증 객체의 서로 다른 동작을 비교합니다. 여러 가지 일반적인 교차 검증 객체를 반복하여 각 객체의 동작을 시각화합니다. 일부 객체는 그룹/클래스 정보를 사용하는 반면, 다른 객체는 사용하지 않는 점에 유의하십시오.

```python
cvs = [
    KFold,
    GroupKFold,
    ShuffleSplit,
    StratifiedKFold,
    StratifiedGroupKFold,
    GroupShuffleSplit,
    StratifiedShuffleSplit,
    TimeSeriesSplit,
]

for cv in cvs:
    this_cv = cv(n_splits=n_splits)
    fig, ax = plt.subplots(figsize=(6, 3))
    plot_cv_indices(this_cv, X, y, groups, ax, n_splits)

    ax.legend(
        [Patch(color=cmap_cv(0.8)), Patch(color=cmap_cv(0.02))],
        ["테스트 세트", "학습 세트"],
        loc=(1.02, 0.8),
    )
    # 범례 크기 조정
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```
