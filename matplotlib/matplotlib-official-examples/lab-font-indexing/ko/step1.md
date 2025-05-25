# 글꼴 로드

먼저, 글꼴 파일을 로드해야 합니다. 이 예제에서는 DejaVuSans.ttf 글꼴 파일을 사용합니다.

```python
import os
import matplotlib
from matplotlib.ft2font import FT2Font

font = FT2Font(os.path.join(matplotlib.get_data_path(), 'fonts/ttf/DejaVuSans.ttf'))
```
