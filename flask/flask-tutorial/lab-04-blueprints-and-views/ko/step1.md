# 블루프린트 생성

애플리케이션을 위한 블루프린트를 생성하는 것으로 시작해 보겠습니다. 이 블루프린트는 'auth'라는 이름으로 지정되며 사용자 인증 관련 뷰를 처리합니다. `flaskr/auth.py`라는 별도의 모듈에서 블루프린트를 정의합니다.

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# Create a Blueprint named 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')
```
