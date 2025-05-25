# RFE 객체 생성 및 데이터 적용

다음으로, RFE 클래스의 객체를 생성하고 데이터를 이 객체에 적용합니다. 추정기로 선형 커널을 사용하는 서포트 벡터 분류기 (SVC) 를 사용할 것입니다. 한 번에 하나의 특징을 선택하고 한 단계씩 진행합니다.

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```
