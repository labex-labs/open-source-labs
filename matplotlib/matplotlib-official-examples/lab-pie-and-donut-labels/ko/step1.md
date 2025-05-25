# 필요한 라이브러리 가져오기 및 서브플롯이 있는 그림 생성

필요한 라이브러리를 가져오고 서브플롯이 있는 그림을 생성하는 것으로 시작합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
```
