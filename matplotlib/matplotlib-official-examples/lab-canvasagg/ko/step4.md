# 렌더러 버퍼를 numpy 배열로 추출

그래프를 저장하는 두 번째 옵션은 렌더러 버퍼를 numpy 배열로 추출하는 것입니다. 이렇게 하면 cgi 스크립트 내에서 Matplotlib 를 사용하여 그래프를 디스크에 쓸 필요가 없습니다. 이 예제에서는 렌더러 버퍼를 추출하여 numpy 배열로 변환합니다.

```python
import numpy as np

canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```
