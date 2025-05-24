# 애플리케이션 팩토리 설정

다음으로, `flaskr` 디렉토리에 `__init__.py` 파일을 생성합니다. 이 파일은 두 가지 목적을 수행합니다. 애플리케이션 팩토리 (application factory) 를 포함하고, Python 에게 `flaskr` 디렉토리를 패키지로 취급해야 함을 알립니다.

`__init__.py` 파일에서 필요한 모듈을 import 하고, 애플리케이션을 인스턴스화하고 구성하는 함수 `create_app()`을 정의합니다.

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # More code to be added here...

    return app
```
