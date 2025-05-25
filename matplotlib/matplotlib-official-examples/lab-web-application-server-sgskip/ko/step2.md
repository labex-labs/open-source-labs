# 의존성 임포트

이 단계에서는 필요한 의존성을 임포트합니다. 이미지 데이터를 인코딩하기 위해 `base64`를 사용하고, 이미지 데이터를 메모리에 저장하기 위해 `BytesIO`를 사용하며, 웹 애플리케이션 서버를 생성하기 위해 `Flask`를 사용하고, 그림을 생성하기 위해 `Figure`를 사용합니다.

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```
