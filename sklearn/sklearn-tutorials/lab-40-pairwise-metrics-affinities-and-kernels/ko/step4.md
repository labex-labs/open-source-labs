# 다항 커널

다항 커널은 두 벡터의 차원 간 상호작용을 고려하여 두 벡터 간의 유사성을 계산합니다.

Scikit-learn 은 벡터 간의 다항 커널을 계산하기 위한 `polynomial_kernel` 함수를 제공합니다.

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# X 와 Y 사이의 다항 커널 계산
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

출력:

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```
