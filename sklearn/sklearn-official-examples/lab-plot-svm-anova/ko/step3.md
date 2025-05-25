# 교차 검증 점수 플롯

특징의 백분위 수에 따른 교차 검증 점수를 플롯합니다.

```python
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

score_means = list()
score_stds = list()
percentiles = (1, 3, 6, 10, 15, 20, 30, 40, 60, 80, 100)

for percentile in percentiles:
    clf.set_params(anova__percentile=percentile)
    this_scores = cross_val_score(clf, X, y)
    score_means.append(this_scores.mean())
    score_stds.append(this_scores.std())

plt.errorbar(percentiles, score_means, np.array(score_stds))
plt.title("선택된 특징의 백분위 수를 변화시킨 SVM-Anova 의 성능")
plt.xticks(np.linspace(0, 100, 11, endpoint=True))
plt.xlabel("백분위 수")
plt.ylabel("정확도 점수")
plt.axis("tight")
plt.show()
```
