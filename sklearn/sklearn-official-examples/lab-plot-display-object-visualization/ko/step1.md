# 데이터 로드 및 모델 학습

이 예제에서는 OpenML 의 혈액 수혈 센터 데이터셋을 사용합니다. 목표는 개인이 혈액을 기증했는지 여부입니다. 먼저 데이터를 학습 및 테스트 데이터셋으로 분할한 다음, 로지스틱 회귀 모델을 학습 데이터셋으로 학습시킵니다.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=1464, return_X_y=True, parser="pandas")
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

clf = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
clf.fit(X_train, y_train)
```
