# 특징 수 대 교차 검증 점수 플롯

선택된 특징 수와 교차 검증 점수를 플롯할 것입니다. 플롯 생성을 위해 matplotlib 를 사용할 것입니다.

```python
import matplotlib.pyplot as plt

n_scores = len(rfecv.cv_results_["mean_test_score"])
plt.figure()
plt.xlabel("선택된 특징 수")
plt.ylabel("평균 테스트 정확도")
plt.errorbar(
    range(min_features_to_select, n_scores + min_features_to_select),
    rfecv.cv_results_["mean_test_score"],
    yerr=rfecv.cv_results_["std_test_score"],
)
plt.title("상관 특징을 가진 재귀적 특징 제거")
plt.show()
```
