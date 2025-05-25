# 학습 및 보정

연결된 학습 및 검증 데이터 (1,000 개 샘플) 로 25 개의 기본 추정자 (트리) 를 사용하여 랜덤 포레스트 분류기를 학습합니다. 이것이 보정되지 않은 분류기입니다.

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

보정된 분류기를 학습하기 위해 동일한 랜덤 포레스트 분류기로 시작하지만, 학습 데이터 하위 집합 (600 개 샘플) 만 사용하여 학습한 다음, `method='sigmoid'`를 사용하여 2 단계 과정에서 검증 데이터 하위 집합 (400 개 샘플) 을 사용하여 보정합니다.

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
