# 定义蓝图

首先，我们将为我们的博客定义一个蓝图。蓝图是一种组织一组相关视图和其他代码的方式。

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# 蓝图名为 'blog'。它在同一个文件中定义。
# 蓝图需要知道它在哪里定义，所以将 __name__ 作为第二个参数传递。
bp = Blueprint('blog', __name__)
```
