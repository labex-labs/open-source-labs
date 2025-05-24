# Configuração Básica

Agora, vamos adicionar alguma configuração básica à nossa aplicação Flask. No mesmo arquivo `app.py`, adicione o seguinte código:

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

A configuração `DEBUG` habilita o modo de depuração (debug mode), que fornece mensagens de erro úteis durante o desenvolvimento. A configuração `SECRET_KEY` é usada para assinar com segurança os cookies de sessão e outras necessidades relacionadas à segurança.

Para acessar os valores da configuração, você pode usar o dicionário `app.config`. Por exemplo, para imprimir o valor da `SECRET_KEY`, adicione o seguinte código à rota `hello`:

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Reinicie a aplicação Flask e visite `http://localhost:5000` para ver a mensagem atualizada com a chave secreta.
