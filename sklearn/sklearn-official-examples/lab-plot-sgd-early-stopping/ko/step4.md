# 결과 플롯

마지막 단계는 결과를 플롯하는 것입니다. 훈련 및 테스트 점수와 반복 횟수 및 학습 시간을 플롯하기 위해 두 개의 서브플롯을 사용할 것입니다. 각 추정기와 중단 기준에 대해 다른 선 스타일을 사용할 것입니다.

```python
# 플롯할 내용 정의
lines = "중단 기준"
x_axis = "max_iter"
styles = ["-.", "--", "-"]

# 첫 번째 플롯: 훈련 및 테스트 점수
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 4))
for ax, y_axis in zip(axes, ["훈련 점수", "테스트 점수"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

# 두 번째 플롯: n_iter 및 학습 시간
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
for ax, y_axis in zip(axes, ["n_iter_", "학습 시간 (초)"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

plt.show()
```
