# 라이브러리 임포트 및 플롯 설정

첫 번째 단계는 필요한 라이브러리를 임포트하고 플롯을 설정하는 것입니다. 이 예제에서는 3D 플롯을 생성하기 위해 Matplotlib 의 `pyplot` 모듈과 `3d` 툴킷을 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')
```
