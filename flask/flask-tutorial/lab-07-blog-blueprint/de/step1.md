# Definiere das Blueprint

Zunächst werden wir ein Blueprint für unseren Blog definieren. Ein Blueprint ist eine Möglichkeit, eine Gruppe von zusammenhängenden Ansichten und anderen Code zu organisieren.

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# Das Blueprint heißt 'blog'. Es wird in der gleichen Datei definiert.
# Das Blueprint muss wissen, wo es definiert ist, daher wird __name__ als zweiter Argument übergeben.
bp = Blueprint('blog', __name__)
```
