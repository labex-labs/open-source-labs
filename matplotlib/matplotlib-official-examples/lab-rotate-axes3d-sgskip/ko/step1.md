# 라이브러리 및 데이터 세트 가져오기

먼저, 필요한 라이브러리와 데이터 세트를 가져와야 합니다. 이 예제에서는 3D 플롯을 생성하기 위해 `matplotlib` 및 `mpl_toolkits.mplot3d` 라이브러리를 사용하고, 샘플 데이터 세트를 생성하기 위해 `axes3d.get_test_data()` 함수를 사용합니다.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```
