# 커널 근사를 위한 Nystroem 방법

Nystroem 방법은 저랭크 근사를 사용하여 커널을 근사하는 일반적인 기술입니다. 커널이 평가되는 데이터셋에서 부분 샘플링을 수행합니다. 기본적으로 RBF 커널을 사용하지만, 모든 커널 함수 또는 사전 계산된 커널 행렬과 함께 사용할 수 있습니다.

커널 근사를 위해 Nystroem 방법을 사용하려면 다음 단계를 따르세요.

1. 원하는 구성 요소 수 (즉, 특징 변환의 대상 차원) 로 Nystroem 객체를 초기화합니다.

```python
from sklearn.kernel_approximation import Nystroem

n_components = 100
nystroem = Nystroem(n_components=n_components)
```

2. Nystroem 객체를 학습 데이터에 맞춥니다.

```python
nystroem.fit(X_train)
```

3. Nystroem 객체를 사용하여 학습 데이터와 테스트 데이터를 변환합니다.

```python
X_train_transformed = nystroem.transform(X_train)
X_test_transformed = nystroem.transform(X_test)
```
