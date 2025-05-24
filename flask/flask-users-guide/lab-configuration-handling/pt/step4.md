# Configuração Baseada em Ambiente

É comum ter diferentes configurações para diferentes ambientes, como desenvolvimento, produção e testes. Flask permite que você alterne as configurações com base em variáveis de ambiente. Crie um novo arquivo chamado `config_dev.py` e adicione o seguinte código:

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

Crie outro arquivo chamado `config_prod.py` com o seguinte código:

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

No arquivo `app.py`, substitua o código de configuração anterior pelo seguinte:

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

A variável de ambiente `FLASK_ENV` é usada para determinar o ambiente. Se estiver definida como `'production'`, a configuração de produção será carregada; caso contrário, a configuração de desenvolvimento será carregada.

Defina a variável de ambiente `FLASK_ENV` como `'production'` e reinicie a aplicação Flask. Visite `http://localhost:5000` para ver a mensagem atualizada com os valores da configuração de produção.
