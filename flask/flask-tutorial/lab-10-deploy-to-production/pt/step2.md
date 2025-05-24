# Instalando a Aplicação no Servidor

Copie o arquivo wheel para o seu servidor. Uma vez lá, configure um novo ambiente virtual Python e instale o arquivo wheel usando pip:

```bash
# Install the wheel file
pip install flaskr-1.0.0-py3-none-any.whl
```

Como este é um novo ambiente, você precisa inicializar o banco de dados novamente:

```bash
# Initialize the database
flask --app flaskr init-db
```
