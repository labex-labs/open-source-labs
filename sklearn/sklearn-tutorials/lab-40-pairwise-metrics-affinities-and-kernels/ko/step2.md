# 커널

커널은 두 개의 객체 간의 유사성을 측정하는 방법입니다. 특징 간의 비선형 관계를 포착하기 위해 다양한 머신 러닝 알고리즘에서 사용될 수 있습니다.

Scikit-learn 은 선형 커널, 다항 커널, 시그모이드 커널, RBF 커널, 라플라시안 커널, 카이제곱 커널과 같은 다양한 커널 함수를 제공합니다.

`pairwise_kernels` 함수를 사용하여 두 개의 샘플 집합 간의 쌍별 커널을 계산해 보겠습니다.

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# 선형 커널을 사용하여 X 와 Y 사이의 쌍별 커널 계산
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

출력:

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```
