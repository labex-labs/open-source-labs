# Configurando a Aplicação

No mesmo arquivo `__init__.py`, adicione os detalhes de configuração necessários para sua aplicação. Isso inclui a configuração de uma chave secreta e a especificação da localização do seu arquivo de banco de dados.

```python
# flaskr/__init__.py

# More code above...

if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'
```
