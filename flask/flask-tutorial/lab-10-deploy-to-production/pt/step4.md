# Executando a Aplicação com um Servidor de Produção

Para um ambiente de produção, você deve usar um servidor WSGI em vez do servidor de desenvolvimento integrado. Usaremos Waitress como nosso servidor WSGI.

Primeiro, instale Waitress:

```bash
# Install Waitress
pip install waitress
```

Agora, diga ao Waitress para servir sua aplicação:

```bash
# Run the application with Waitress
waitress-serve --call 'flaskr:create_app'
```
