# 创建一个蓝图

让我们从为我们的应用程序创建一个蓝图开始。这个蓝图将被命名为“auth”，并将处理与用户认证相关的视图。我们将在一个名为`flaskr/auth.py`的单独模块中定义我们的蓝图。

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# 创建一个名为“auth”的蓝图
bp = Blueprint('auth', __name__, url_prefix='/auth')
```
