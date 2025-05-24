# Blueprint 정의

먼저, 블로그를 위한 Blueprint 를 정의합니다. Blueprint 는 관련 뷰 (view) 및 기타 코드를 그룹화하여 구성하는 방법입니다.

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# Blueprint 는 'blog'로 명명됩니다. 동일한 파일에서 정의됩니다.
# Blueprint 는 정의된 위치를 알아야 하므로 __name__이 두 번째 인수로 전달됩니다.
bp = Blueprint('blog', __name__)
```
