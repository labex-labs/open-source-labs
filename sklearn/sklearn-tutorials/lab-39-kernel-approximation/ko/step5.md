# 텐서 스케치를 통한 다항식 커널 근사

다항식 커널은 특징 간의 상호작용을 모델링하는 인기 있는 커널 함수입니다. PolynomialCountSketch 클래스는 텐서 스케치 접근 방식을 사용하여 이 커널을 근사하는 확장 가능한 방법을 제공합니다.

PolynomialCountSketch 를 사용하여 커널 근사를 하려면 다음 단계를 따르세요.

1. 원하는 차수 (d) 와 구성 요소 수로 PolynomialCountSketch 객체를 초기화합니다.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

degree = 3
n_components = 100
polynomial_count_sketch = PolynomialCountSketch(degree=degree, n_components=n_components)
```

2. PolynomialCountSketch 객체를 학습 데이터에 맞춥니다.

```python
polynomial_count_sketch.fit(X_train)
```

3. PolynomialCountSketch 객체를 사용하여 학습 데이터와 테스트 데이터를 변환합니다.

```python
X_train_transformed = polynomial_count_sketch.transform(X_train)
X_test_transformed = polynomial_count_sketch.transform(X_test)
```
