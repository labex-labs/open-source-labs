# Pasta de Instância

Flask fornece uma pasta de instância para armazenar arquivos de configuração que são específicos para uma implantação particular. Isso permite que você separe as configurações específicas da implantação do restante do seu código. Por padrão, Flask usa uma pasta chamada `instance` no mesmo diretório da sua aplicação.

Crie uma nova pasta chamada `instance` no mesmo diretório do seu arquivo `app.py`. Na pasta `instance`, crie um arquivo chamado `config.cfg` e adicione o seguinte código:

```
DEBUG = True
SECRET_KEY = 'instancekey'
```

No arquivo `app.py`, adicione o seguinte código antes do código de configuração:

```python
app.instance_path = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile('config.cfg')
```

O `instance_path` é definido para o caminho absoluto da pasta `instance`. O método `from_pyfile` carrega a configuração do arquivo `config.cfg` na pasta de instância.

Reinicie a aplicação Flask e visite `http://localhost:5000` para ver a mensagem atualizada com os valores da configuração da instância.
