# 유병률에 대한 불변성

질병 가능도 비율은 질병 유병률과 무관하며, 어떠한 클래스 불균형에도 관계없이 인구 집단 간에 외삽될 수 있음을 보여줍니다.

## 데이터 준비

`make_classification` 함수를 사용하여 scikit-learn 에서 합성 데이터 세트를 생성합니다. 이 데이터 세트는 질병을 가진 피험자의 비율이 적은 인구를 시뮬레이션합니다.

```python
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=10_000, weights=[0.9, 0.1], random_state=0)
print(f"질병을 가진 사람의 비율: {100*y.mean():.2f}%")
```

## 사전 검사 대 사후 검사 분석

데이터에 로지스틱 회귀 모델을 적합하고, 보류된 테스트 세트에서 성능을 평가합니다. 이 분류기가 질병 진단 도구로서의 유용성을 평가하기 위해 양성 가능도 비율을 계산합니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import class_likelihood_ratios
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

estimator = LogisticRegression().fit(X_train, y_train)
y_pred = estimator.predict(X_test)
pos_LR, neg_LR = class_likelihood_ratios(y_test, y_pred)

print(f"LR+: {pos_LR:.3f}")
```

## 가능도 비율의 교차 검증

특정 경우에 대한 클래스 가능도 비율 측정의 변동성을 교차 검증을 통해 평가합니다.

```python
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.dummy import DummyClassifier

def scoring(estimator, X, y):
    y_pred = estimator.predict(X)
    pos_lr, neg_lr = class_likelihood_ratios(y, y_pred, raise_warning=False)
    return {"positive_likelihood_ratio": pos_lr, "negative_likelihood_ratio": neg_lr}

def extract_score(cv_results):
    lr = pd.DataFrame(
        {
            "positive": cv_results["test_positive_likelihood_ratio"],
            "negative": cv_results["test_negative_likelihood_ratio"],
        }
    )
    return lr.aggregate(["mean", "std"])

estimator = LogisticRegression()
extract_score(cross_validate(estimator, X, y, scoring=scoring, cv=10))

estimator = DummyClassifier(strategy="stratified", random_state=1234)
extract_score(cross_validate(estimator, X, y, scoring=scoring, cv=10))

estimator = DummyClassifier(strategy="most_frequent")
extract_score(cross_validate(estimator, X, y, scoring=scoring, cv=10))
```

## 유병률에 대한 불변성

질병 가능도 비율은 질병 유병률과 무관하며, 어떠한 클래스 불균형에도 관계없이 인구 집단 간에 외삽될 수 있음을 보여줍니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from collections import defaultdict

# ... (나머지 코드 생략)
```
