# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) é um ataque que engana usuários para que realizem ações não intencionais em um website. Para prevenir ataques CSRF em Flask, siga estas diretrizes:

- Use tokens de uso único para validar requisições que modificam o conteúdo do servidor.
- Armazene o token no cookie e transmita-o com os dados do formulário.
- Compare o token recebido no servidor com aquele armazenado no cookie.

Exemplo de código:

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

Para executar o código, salve-o em um arquivo chamado `app.py` e execute o comando `flask run`.
