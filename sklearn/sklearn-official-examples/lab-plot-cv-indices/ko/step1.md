# 데이터 시각화

이 단계에서는 작업할 데이터를 시각화합니다. 데이터는 100 개의 임의로 생성된 입력 데이터 포인트, 데이터 포인트에 불균형적으로 분포된 3 개의 클래스, 그리고 데이터 포인트에 균등하게 분포된 10 개의 "그룹"으로 구성됩니다.

```python
# 클래스/그룹 데이터 생성
n_points = 100
X = rng.randn(100, 10)

percentiles_classes = [0.1, 0.3, 0.6]
y = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentiles_classes)])

# 불균등한 그룹 생성
group_prior = rng.dirichlet([2] * 10)
groups = np.repeat(np.arange(10), rng.multinomial(100, group_prior))


def visualize_groups(classes, groups, name):
    # 데이터셋 그룹 시각화
    fig, ax = plt.subplots()
    ax.scatter(
        range(len(groups)),
        [0.5] * len(groups),
        c=groups,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.scatter(
        range(len(groups)),
        [3.5] * len(groups),
        c=classes,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.set(
        ylim=[-1, 5],
        yticks=[0.5, 3.5],
        yticklabels=["데이터\n그룹", "데이터\n클래스"],
        xlabel="샘플 인덱스",
    )


visualize_groups(y, groups, "no groups")
```
