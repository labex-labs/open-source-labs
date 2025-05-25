# 라이브러리 임포트 및 상자 스타일 가져오기

이 단계에서는 필요한 라이브러리를 임포트하고 플로팅에 사용할 상자 스타일을 가져오겠습니다.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```
