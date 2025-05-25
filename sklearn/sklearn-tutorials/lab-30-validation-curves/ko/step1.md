# 필요한 라이브러리 가져오기 및 데이터 로드

필요한 라이브러리를 가져오고 데이터 세트를 로드하는 것으로 시작하겠습니다. 이 예제에서는 Iris 데이터 세트를 사용합니다.

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```
