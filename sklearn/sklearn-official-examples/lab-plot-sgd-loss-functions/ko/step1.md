# 라이브러리 가져오기 및 함수 정의

필요한 라이브러리를 가져오고 수정된 Huber 손실 함수를 정의합니다.

```python
import numpy as np
import matplotlib.pyplot as plt

def modified_huber_loss(y_true, y_pred):
    z = y_pred * y_true
    loss = -4 * z
    loss[z >= -1] = (1 - z[z >= -1]) ** 2
    loss[z >= 1.0] = 0
    return loss
```
