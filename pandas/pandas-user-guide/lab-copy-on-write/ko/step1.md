# Copy-On-Write 활성화

먼저, pandas 에서 CoW 를 활성화해 보겠습니다. 이는 pandas 의 `copy_on_write` 구성 옵션을 사용하여 수행할 수 있습니다. CoW 를 전역적으로 활성화하는 두 가지 방법은 다음과 같습니다.

```python
# pandas 및 numpy 라이브러리 가져오기
import pandas as pd

# set_option 을 사용하여 CoW 활성화
pd.set_option("mode.copy_on_write", True)

# 또는 직접 할당 사용
pd.options.mode.copy_on_write = True
```
