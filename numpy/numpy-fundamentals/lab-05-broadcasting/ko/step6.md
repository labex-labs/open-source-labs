# 실용적인 예시 - 벡터 양자화 (Vector Quantization)

브로드캐스팅이 유용한 실용적인 예시를 살펴보겠습니다. 정보 이론 및 분류에 사용되는 벡터 양자화 (VQ) 알고리즘을 고려해 보겠습니다. VQ 의 기본 연산은 주어진 점에 가장 가까운 점을 일련의 점들에서 찾는 것입니다. 이는 브로드캐스팅을 사용하여 수행할 수 있습니다. 다음은 예시입니다.

```python
import numpy as np

observation = np.array([111.0, 188.0])
codes = np.array([[102.0, 203.0],
                  [132.0, 193.0],
                  [45.0, 155.0],
                  [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2, axis=-1))
closest_index = np.argmin(dist)
closest_code = codes[closest_index]
```

이 예시에서 `observation`은 분류할 운동 선수의 몸무게와 키를 나타내고, `codes`는 서로 다른 운동 선수 클래스를 나타냅니다. `observation`을 `codes`에서 빼면, 브로드캐스팅을 사용하여 `observation`과 각 코드 간의 거리를 계산합니다. 그런 다음 `argmin` 함수를 사용하여 가장 가까운 코드의 인덱스를 찾습니다.
