# 결과 시각화

Plotly.express 를 사용하여 하이퍼파라미터 튜닝 결과를 시각화할 수 있습니다. 점 산점도를 사용하여 평균 테스트 점수와 스코어링 시간 간의 트레이드오프를 시각화합니다. 또한 평행 좌표를 사용하여 조정된 하이퍼파라미터의 함수로서 평균 테스트 점수를 추가적으로 시각화할 수 있습니다.

```python
import pandas as pd
import plotly.express as px
import math

def shorten_param(param_name):
    """Remove components' prefixes in param_name."""
    if "__" in param_name:
        return param_name.rsplit("__", 1)[1]
    return param_name

cv_results = pd.DataFrame(random_search.cv_results_)
cv_results = cv_results.rename(shorten_param, axis=1)

param_names = [shorten_param(name) for name in parameter_grid.keys()]
labels = {
    "mean_score_time": "CV 스코어 시간 (초)",
    "mean_test_score": "CV 스코어 (정확도)",
}
fig = px.scatter(
    cv_results,
    x="mean_score_time",
    y="mean_test_score",
    error_x="std_score_time",
    error_y="std_test_score",
    hover_data=param_names,
    labels=labels,
)

fig.update_layout(
    title={
        "text": "스코어링 시간과 평균 테스트 점수 간의 트레이드오프",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

column_results = param_names + ["mean_test_score", "mean_score_time"]

transform_funcs = dict.fromkeys(column_results, lambda x: x)
# alpha 에 대한 로그 스케일 사용
transform_funcs["alpha"] = math.log10
# L1 정규화는 인덱스 1, L2 정규화는 인덱스 2 에 매핑
transform_funcs["norm"] = lambda x: 2 if x == "l2" else 1
# unigram 은 인덱스 1, bigram 은 인덱스 2 에 매핑
transform_funcs["ngram_range"] = lambda x: x[1]

fig = px.parallel_coordinates(
    cv_results[column_results].apply(transform_funcs),
    color="mean_test_score",
    color_continuous_scale=px.colors.sequential.Viridis_r,
    labels=labels,
)
fig.update_layout(
    title={
        "text": "텍스트 분류기 파이프라인의 평행 좌표 플롯",
        "y": 0.99,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

```
