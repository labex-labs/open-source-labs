# 무작위 데이터 생성

먼저, 0 과 1 사이의 1000 개의 무작위 숫자를 각각 포함하는 100 개의 무작위 데이터 세트를 생성해야 합니다. numpy 의 random 모듈을 사용하여 무작위 데이터를 생성합니다.

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```
