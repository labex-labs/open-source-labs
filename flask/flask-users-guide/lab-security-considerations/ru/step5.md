# Set-Cookie Options

При установке cookie в Flask важно учитывать параметры безопасности для защиты конфиденциальных данных. Некоторые рекомендуемые параметры:

- Secure: ограничивает cookie только для HTTPS-трафика.
- HttpOnly: защищает содержимое cookie от чтения с помощью JavaScript.
- SameSite: ограничивает способ передачи cookie с запросами от внешних сайтов.

Пример кода:

```python
# app.py

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello, world!')
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run()
```

Для запуска кода сохраните его в файл с именем `app.py` и выполните команду `flask run`.
