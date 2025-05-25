# Additive Chi Squared (ACS) 커널 근사

ACS 커널은 컴퓨터 비전에서 일반적으로 사용되는 히스토그램에 대한 커널입니다. AdditiveChi2Sampler 클래스는 이 커널에 대한 근사 매핑을 제공합니다.

AdditiveChi2Sampler 를 사용하여 커널 근사를 하려면 다음 단계를 따르세요.

1. 원하는 샘플 수 (n) 와 정규화 매개변수 (c) 로 AdditiveChi2Sampler 객체를 초기화합니다.

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. AdditiveChi2Sampler 객체를 학습 데이터에 맞춥니다.

```python
additive_chi2_sampler.fit(X_train)
```

3. AdditiveChi2Sampler 객체를 사용하여 학습 데이터와 테스트 데이터를 변환합니다.

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```
