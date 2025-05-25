# 필요한 라이브러리 가져오기 및 상수 정의

먼저, 다중 레이블 데이터셋을 생성하기 위해 필요한 라이브러리를 가져오고 색상 및 랜덤 시드 상수를 정의해야 합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification as make_ml_clf

COLORS = np.array(
    [
        "!",
        "#FF3333",  # 빨강
        "#0198E1",  # 파랑
        "#BF5FFF",  # 보라
        "#FCD116",  # 노랑
        "#FF7216",  # 주황
        "#4DBD33",  # 초록
        "#87421F",  # 갈색
    ]
)

# make_multilabel_classification 함수를 여러 번 호출할 때 동일한 랜덤 시드를 사용하여
# 동일한 분포를 보장합니다.
RANDOM_SEED = np.random.randint(2**10)
```
