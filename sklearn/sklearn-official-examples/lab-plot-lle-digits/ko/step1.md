# 숫자 데이터셋 로드

이번 실습에서는 숫자 데이터셋을 로드하고, 사용 가능한 10 개 클래스 중 6 개만 사용합니다. 또한, 이 데이터셋에서 처음 100 개의 숫자를 플롯합니다.

```python
# 숫자 데이터셋 로드
from sklearn.datasets import load_digits

digits = load_digits(n_class=6)
X, y = digits.data, digits.target
n_samples, n_features = X.shape
n_neighbors = 30

# 처음 100 개 숫자 플롯
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(6, 6))
for idx, ax in enumerate(axs.ravel()):
    ax.imshow(X[idx].reshape((8, 8)), cmap=plt.cm.binary)
    ax.axis("off")
_ = fig.suptitle("64 차원 숫자 데이터셋에서 선택된 샘플", fontsize=16)
```
