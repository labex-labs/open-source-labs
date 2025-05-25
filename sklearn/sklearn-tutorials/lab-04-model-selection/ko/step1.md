# 점수 및 교차 검증 점수

scikit-learn 의 추정자는 `score` 메서드를 통해 새 데이터에 대한 모델의 적합도 또는 예측의 품질을 평가하는 데 사용할 수 있습니다. 이 메서드는 점수를 반환하며, 값이 높을수록 성능이 더 좋습니다.

```python
from sklearn import datasets, svm

# 숫자 데이터셋 로드
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# 선형 커널을 사용하는 SVM 분류기 생성
svc = svm.SVC(C=1, kernel='linear')

# 학습 데이터에 분류기를 맞추고 테스트 데이터에 대한 점수 계산
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

예측 정확도를 더 잘 측정하기 위해 교차 검증을 사용할 수 있습니다. 교차 검증은 데이터를 여러 폴드로 나누고 각 폴드를 테스트 세트로 사용하고 나머지 폴드를 학습 세트로 사용하는 것을 포함합니다. 이 과정을 여러 번 반복하고 점수를 평균하여 전체 성능을 얻습니다.

```python
import numpy as np

# 데이터를 3 개의 폴드로 분할
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# 교차 검증 수행
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
