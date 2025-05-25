# 아이리스 데이터셋 로드 및 분할

머신러닝 분류 작업에서 널리 사용되는 아이리스 데이터셋을 로드합니다. 이 데이터셋은 각각 꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비의 네 가지 특징을 가진 150 개의 아이리스 꽃 샘플을 포함합니다. 데이터셋을 입력 특징과 목표 레이블로 분할합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# 아이리스 데이터셋 로드
iris = datasets.load_iris()

# 데이터셋을 입력 특징과 목표 레이블로 분할
X = iris.data[:, :2] # 시각화를 위해 처음 두 특징만 사용합니다
y = iris.target
```
