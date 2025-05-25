# 임포트에 대한 주석

import 의 변형은 모듈의 작동 방식을 _변경하지_ 않습니다.

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

구체적으로, `import`는 항상 _전체_ 파일을 실행하며 모듈은 여전히 격리된 환경입니다.

`import module as` 구문은 로컬에서 이름만 변경합니다. `from math import cos, sin` 구문은 여전히 백그라운드에서 전체 math 모듈을 로드합니다. 이는 단순히 완료된 후 `cos` 및 `sin` 이름을 모듈에서 로컬 공간으로 복사하는 것입니다.
