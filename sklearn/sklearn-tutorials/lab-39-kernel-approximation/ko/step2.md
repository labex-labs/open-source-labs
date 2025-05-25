# Radial Basis Function (RBF) 커널 근사

RBFSampler 클래스는 RBF 커널에 대한 근사 매핑을 구현합니다. 이 기술은 선형 SVM 이나 로지스틱 회귀와 같은 선형 알고리즘을 적용하기 전에 커널 매핑을 명시적으로 모델링할 수 있도록 합니다.

RBFSampler 를 사용하여 커널 근사를 하려면 다음 단계를 따르세요.

1. 원하는 감마 값 (RBF 커널의 매개변수) 과 구성 요소 수로 RBFSampler 객체를 초기화합니다.

```python
from sklearn.kernel_approximation import RBFSampler

gamma = 0.1
n_components = 100
rbf_sampler = RBFSampler(gamma=gamma, n_components=n_components)
```

2. RBFSampler 객체를 학습 데이터에 맞춥니다.

```python
rbf_sampler.fit(X_train)
```

3. RBFSampler 객체를 사용하여 학습 데이터와 테스트 데이터를 변환합니다.

```python
X_train_transformed = rbf_sampler.transform(X_train)
X_test_transformed = rbf_sampler.transform(X_test)
```
