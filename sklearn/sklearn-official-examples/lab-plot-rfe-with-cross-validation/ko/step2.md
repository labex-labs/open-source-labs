# 모델 학습 및 선택

RFECV 객체를 생성하고 교차 검증 점수를 계산할 것입니다. "정확도" 점수 전략은 올바르게 분류된 샘플의 비율을 최적화합니다. 로지스틱 회귀를 추정기로 사용하고 5 개의 폴드를 가진 계층적 k-겹 교차 검증을 사용할 것입니다.

```python
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

min_features_to_select = 1  # 고려할 최소 특징 수
clf = LogisticRegression()
cv = StratifiedKFold(5)

rfecv = RFECV(
    estimator=clf,
    step=1,
    cv=cv,
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
    n_jobs=2,
)
rfecv.fit(X, y)

print(f"최적 특징 수: {rfecv.n_features_}")
```
