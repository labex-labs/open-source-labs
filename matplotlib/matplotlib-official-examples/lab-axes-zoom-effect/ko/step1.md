# 필요한 라이브러리 가져오기

이 단계에서는 이 튜토리얼에 필요한 필수 라이브러리를 가져오겠습니다. matplotlib 과 mpl_toolkits.axes_grid1 에서 관련 라이브러리를 가져오겠습니다.

```python
import matplotlib.pyplot as plt

from matplotlib.transforms import (Bbox, TransformedBbox,
                                   blended_transform_factory)
from mpl_toolkits.axes_grid1.inset_locator import (BboxConnector,
                                                   BboxConnectorPatch,
                                                   BboxPatch)
```
