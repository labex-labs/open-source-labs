# 결과 플롯

`GridSearchCV`의 결과를 막대 그래프로 플롯하여 서로 다른 특징 축소 기법의 정확도를 비교합니다.

```python
import pandas as pd

mean_scores = np.array(grid.cv_results_["mean_test_score"])
# 점수는 param_grid 반복 순서 (사전순) 에 따라 정렬되어 있습니다.
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))
# 최적의 C 에 대한 점수를 선택합니다.
mean_scores = mean_scores.max(axis=0)
# 플롯을 쉽게 하기 위해 데이터프레임을 생성합니다.
mean_scores = pd.DataFrame(
    mean_scores.T, index=N_FEATURES_OPTIONS, columns=reducer_labels
)

ax = mean_scores.plot.bar()
ax.set_title("특징 축소 기법 비교")
ax.set_xlabel("축소된 특징 개수")
ax.set_ylabel("숫자 분류 정확도")
ax.set_ylim((0, 1))
ax.legend(loc="upper left")

plt.show()
```
