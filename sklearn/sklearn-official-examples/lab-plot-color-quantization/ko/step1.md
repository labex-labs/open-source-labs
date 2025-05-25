# 원본 이미지 로드 및 표시

여름궁전의 원본 이미지를 로드하고 표시하는 것으로 시작하겠습니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# 여름궁전 사진 로드
china = load_sample_image("china.jpg")

# 원본 이미지 표시
plt.figure()
plt.axis("off")
plt.title("원본 이미지")
plt.imshow(china)
plt.show()
```
