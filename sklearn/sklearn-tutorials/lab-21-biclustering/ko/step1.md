# 필요한 라이브러리 및 데이터셋 가져오기

먼저, 양분할 군집화 (biclustering) 에 사용할 필요한 라이브러리를 가져오고 샘플 데이터셋을 로드합니다.

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# 샘플 데이터 로드
data = np.arange(100).reshape(10, 10)
```
