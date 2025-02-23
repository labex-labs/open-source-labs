# ブループリントを定義する

まず、ブログ用のブループリントを定義します。ブループリントは、関連するビューやその他のコードのグループを整理する方法です。

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# ブループリントは 'blog' と名付けられています。同じファイル内で定義されています。
# ブループリントは自分自身が定義されている場所を知る必要があるため、2番目の引数として __name__ が渡されます。
bp = Blueprint('blog', __name__)
```
