# Определение Blueprint

Во - первых, мы определим Blueprint для нашего блога. Blueprint - это способ организации группы связанных представлений и другого кода.

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# Blueprint назван 'blog'. Он определяется в том же файле.
# Blueprint должен знать, где он определен, поэтому __name__ передается в качестве второго аргумента.
bp = Blueprint('blog', __name__)
```
