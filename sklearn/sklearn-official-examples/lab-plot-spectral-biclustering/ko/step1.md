# 샘플 데이터 생성

`make_checkerboard` 함수를 사용하여 샘플 데이터를 생성합니다. `shape=(300, 300)` 내의 각 픽셀은 고르게 분포된 값을 색상으로 나타냅니다. 노이즈는 정규 분포에서 추가되며, `noise`에 선택된 값은 표준 편차입니다.

```python
from sklearn.datasets import make_checkerboard
from matplotlib import pyplot as plt

n_clusters = (4, 3)
data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10, shuffle=False, random_state=42
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
_ = plt.show()
```
