# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) - это атака, которая обманчивает пользователей выполнять непреднамеренные действия на веб-сайте. Чтобы предотвратить атаки CSRF в Flask, следуйте этим рекомендациям:

- Используйте одноразовые токены для проверки запросов, которые изменяют содержимое сервера.
- Сохраняйте токен в cookie и передавайте его вместе с данными формы.
- Сравните токен, полученный на сервере, с тем, который хранится в cookie.

Пример кода:

```python
# app.py

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        token = request.form.get('token')
        if token and token == session.get('csrf_token'):
            # Delete user profile
            return redirect(url_for('index'))
    return 'Invalid request'

if __name__ == '__main__':
    app.run()
```

Для запуска кода сохраните его в файл с именем `app.py` и выполните команду `flask run`.
