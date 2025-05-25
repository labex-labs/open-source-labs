# 데이터셋 로드

20 개의 주제에 대한 약 18,000 개의 뉴스그룹 게시물을 포함하는 20 뉴스그룹 데이터셋을 사용할 것입니다. 이 단계에서는 데이터셋을 로드하고 데이터셋에 대한 기본 정보를 출력합니다.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# 처음 5 개 카테고리로 데이터셋 로드
data = fetch_20newsgroups(
    subset="train",
    categories=[
        "alt.atheism",
        "comp.graphics",
        "comp.os.ms-windows.misc",
        "comp.sys.ibm.pc.hardware",
        "comp.sys.mac.hardware",
    ],
)

# 데이터셋 정보 출력
print("%d documents" % len(data.filenames))
print("%d categories" % len(data.target_names))
```
