# Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) - это уязвимость, которая позволяет атакующим внедрять вредоносные скрипты в веб-страницы, которые просматривают пользователи. Чтобы предотвратить атаки XSS в Flask, следуйте этим рекомендациям:

- Всегда экранируйте текст, чтобы предотвратить включение произвольных HTML-тегов.
- Будьте осторожны при генерации HTML без помощи шаблонов Jinja2.
- Используйте класс `Markup` для экранирования данных, введенных пользователем.
- Избегайте отправки HTML- или текстовых файлов из загруженных файлов.

Пример кода:

```python
# app.py

from flask import Flask, render_template_string, Markup

app = Flask(__name__)

@app.route('/')
def index():
    value = '<script>alert("XSS Attack")</script>'
    safe_value = Markup.escape(value)
    return render_template_string('<input value="{{ value }}">', value=safe_value)
```

Для запуска кода сохраните его в файл с именем `app.py` и выполните команду `flask run`.
