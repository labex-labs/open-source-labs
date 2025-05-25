# 시작 옵션 설정하기

pandas 를 가져오고 옵션을 설정하는 시작 스크립트를 Python/IPython 환경에서 생성하여 pandas 작업을 더욱 효율적으로 만들 수 있습니다.

```python
# This is an example of a startup script
# Place this in a .py file in the startup directory of IPython profile
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```
