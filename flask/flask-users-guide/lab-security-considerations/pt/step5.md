# Opções de Set-Cookie

Ao definir cookies em Flask, é importante considerar as opções de segurança para proteger dados sensíveis. Algumas opções recomendadas são:

- Secure: Limita os cookies apenas ao tráfego HTTPS.
- HttpOnly: Protege o conteúdo dos cookies de serem lidos com JavaScript.
- SameSite: Restringe como os cookies são enviados com requisições de sites externos.

Exemplo de código:

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

Para executar o código, salve-o em um arquivo chamado `app.py` e execute o comando `flask run`.
