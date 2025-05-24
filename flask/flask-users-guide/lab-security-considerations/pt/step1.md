# Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) é uma vulnerabilidade que permite que atacantes injetem scripts maliciosos em páginas web visualizadas por usuários. Para prevenir ataques XSS em Flask, siga estas diretrizes:

- Sempre faça o escape do texto para evitar a inclusão de tags HTML arbitrárias.
- Seja cauteloso ao gerar HTML sem a ajuda de templates Jinja2.
- Use a classe `Markup` para fazer o escape de dados enviados pelo usuário.
- Evite enviar arquivos HTML ou de texto a partir de arquivos carregados.

Exemplo de código:

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

Para executar o código, salve-o em um arquivo chamado `app.py` e execute o comando `flask run`.
