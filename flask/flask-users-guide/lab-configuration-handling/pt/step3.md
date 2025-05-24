# Configuração de Arquivos

Codificar os valores de configuração diretamente no código não é ideal, especialmente para informações sensíveis. Flask oferece uma maneira de carregar a configuração de arquivos separados. Crie um novo arquivo chamado `config.py` e adicione o seguinte código:

```python
DEBUG = False
SECRET_KEY = 'myothersecretkey'
```

No arquivo `app.py`, substitua o código de configuração anterior pelo seguinte:

```python
app.config.from_object('config')
```

O método `from_object` carrega a configuração do módulo `config`. Agora, os valores `DEBUG` e `SECRET_KEY` serão carregados do arquivo `config.py`.

Reinicie a aplicação Flask e visite `http://localhost:5000` para ver a mensagem atualizada com os novos valores de configuração.
