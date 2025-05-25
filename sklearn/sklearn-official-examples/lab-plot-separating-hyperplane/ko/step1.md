# 이진 분류 가능 데이터셋 생성

이진 분류가 가능한 데이터셋을 생성하기 위해 scikit-learn 의 `make_blobs()` 함수를 사용합니다. 이 함수는 클러스터링 및 분류를 위해 등방성 가우시안 덩어리 (blobs) 를 생성합니다. 2 개의 중심과 난수 시드 6 을 사용하여 40 개의 샘플을 생성합니다. 또한 `matplotlib`를 사용하여 데이터 포인트를 플롯합니다.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# 이진 분류 가능 데이터셋 생성
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# 데이터 포인트 플롯
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
