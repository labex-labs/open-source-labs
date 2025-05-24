# Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) 는 공격자가 사용자가 보는 웹 페이지에 악성 스크립트를 주입할 수 있도록 하는 취약점입니다. Flask 에서 XSS 공격을 방지하려면 다음 지침을 따르십시오.

- 항상 텍스트를 이스케이프하여 임의의 HTML 태그가 포함되는 것을 방지합니다.
- Jinja2 템플릿의 도움 없이 HTML 을 생성할 때는 주의하십시오.
- `Markup` 클래스를 사용하여 사용자가 제출한 데이터를 이스케이프합니다.
- 업로드된 파일에서 HTML 또는 텍스트 파일을 보내는 것을 피하십시오.

예제 코드:

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

코드를 실행하려면 `app.py`라는 파일에 저장하고 `flask run` 명령을 실행하십시오.
