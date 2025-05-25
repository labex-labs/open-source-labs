# 정규화 경로 계산

다양한 정규화 강도를 가진 L1-페널티화된 로지스틱 회귀 모델을 학습하여 정규화 경로를 계산할 것입니다. liblinear 솔버를 사용하여 L1 페널티가 있는 로지스틱 회귀 손실을 효율적으로 최적화할 것입니다. 모델이 계수를 수집하기 전에 수렴했는지 확인하기 위해 허용 오차 (tolerance) 를 낮은 값으로 설정할 것입니다. 또한 warm_start=True 를 사용하여 이전 모델의 계수를 다음 모델의 초기화에 재사용하여 전체 경로 계산 속도를 높일 것입니다.

```python
import numpy as np
from sklearn import linear_model
from sklearn.svm import l1_min_c

cs = l1_min_c(X, y, loss="log") * np.logspace(0, 10, 16)

clf = linear_model.LogisticRegression(
    penalty="l1",
    solver="liblinear",
    tol=1e-6,
    max_iter=int(1e6),
    warm_start=True,
    intercept_scaling=10000.0,
)
coefs_ = []
for c in cs:
    clf.set_params(C=c)
    clf.fit(X, y)
    coefs_.append(clf.coef_.ravel().copy())

coefs_ = np.array(coefs_)
```
