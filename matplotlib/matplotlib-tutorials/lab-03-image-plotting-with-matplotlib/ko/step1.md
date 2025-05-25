# 이미지 데이터 가져오기

시작하기 위해 필요한 라이브러리를 가져오고 이미지 데이터를 NumPy 배열로 로드해야 합니다. 이 경우, `PIL` 라이브러리를 사용하여 이미지를 로드한 다음, NumPy 배열로 변환합니다.

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
