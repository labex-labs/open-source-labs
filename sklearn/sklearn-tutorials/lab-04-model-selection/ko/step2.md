# 교차 검증 생성기

Scikit-learn 은 인기 있는 교차 검증 전략에 대한 학습/테스트 인덱스를 생성하는 데 사용할 수 있는 클래스 모음을 제공합니다. 이러한 클래스는 `split` 메서드를 가지고 있으며, 입력 데이터 세트를 받아 교차 검증 프로세스의 각 반복에 대한 학습/테스트 세트 인덱스를 생성합니다.

```python
from sklearn.model_selection import KFold

# KFold 교차 검증을 사용하여 데이터를 K 개의 폴드로 분할
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'Train: {train_indices} | test: {test_indices}')
```

`cross_val_score` 도우미 함수는 교차 검증 점수를 직접 계산하는 데 사용할 수 있습니다. 데이터를 각 교차 검증 반복에 대한 학습 및 테스트 세트로 분할하고, 추정자를 학습 세트에 훈련시키며, 테스트 세트를 기반으로 점수를 계산합니다.

```python
from sklearn.model_selection import cross_val_score

# SVM 분류기의 교차 검증 점수 계산
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```
