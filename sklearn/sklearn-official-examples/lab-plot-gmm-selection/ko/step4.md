# BIC 점수 플롯

그리드 검색으로 수행된 교차 검증 결과에서 `pandas.DataFrame`을 생성합니다. BIC 점수의 부호를 다시 반전하여 최소화 효과를 보여줍니다. `seaborn`을 사용하여 BIC 점수를 플롯합니다.

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame(grid_search.cv_results_)[
    ["param_n_components", "param_covariance_type", "mean_test_score"]
]
df["mean_test_score"] = -df["mean_test_score"]
df = df.rename(
    columns={
        "param_n_components": "구성 요소 수",
        "param_covariance_type": "공분산 유형",
        "mean_test_score": "BIC 점수",
    }
)
df.sort_values(by="BIC 점수").head()

sns.catplot(
    data=df,
    kind="bar",
    x="구성 요소 수",
    y="BIC 점수",
    hue="공분산 유형",
)
plt.show()
```
