# Configurando a Chave Secreta

Em um ambiente de produção, você deve alterar a chave secreta para um valor aleatório. Para gerar uma chave secreta aleatória, execute o seguinte comando:

```bash
# Generate a random secret key
python -c 'import secrets; print(secrets.token_hex())'
```

Crie um arquivo `config.py` na pasta instance e defina `SECRET_KEY` para o valor gerado.

```python
# .venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```
