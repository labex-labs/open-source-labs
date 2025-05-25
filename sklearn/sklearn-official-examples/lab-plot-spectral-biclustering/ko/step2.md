# 데이터 섞기

데이터를 섞고 나중에 `SpectralBiclustering`를 사용하여 재구성하는 것이 목표입니다.

```python
import numpy as np

# 섞인 행 및 열 인덱스의 리스트 생성
rng = np.random.RandomState(0)
row_idx_shuffled = rng.permutation(data.shape[0])
col_idx_shuffled = rng.permutation(data.shape[1])

# 섞인 데이터를 재정의하고 플롯합니다.
data = data[row_idx_shuffled][:, col_idx_shuffled]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("섞인 데이터 세트")
_ = plt.show()
```
