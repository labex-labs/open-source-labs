# 데이터 생성

먼저, 125 개의 샘플과 2 개의 특징을 가진 데이터 집합을 생성합니다. 두 특징 모두 평균이 0 인 가우시안 분포를 따릅니다. 그러나 특징 1 의 표준 편차는 2 이고, 특징 2 의 표준 편차는 1 입니다. 다음으로, 특징 1 의 표준 편차가 1 이고 특징 2 의 표준 편차가 7 인 가우시안 이상치 샘플로 25 개의 샘플을 대체합니다.

```python
import numpy as np

# 일관된 결과를 위해
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# 모양이 (125, 2) 인 가우시안 데이터 생성
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# 이상치 추가
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
