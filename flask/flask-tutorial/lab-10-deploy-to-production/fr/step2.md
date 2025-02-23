# Install the Application on the Server

Copiez le fichier wheel sur votre serveur. Une fois que vous y êtes, configurez un nouvel environnement virtuel Python et installez le fichier wheel avec pip :

```bash
# Install the wheel file
pip install flaskr-1.0.0-py3-none-any.whl
```

Puisque c'est un nouvel environnement, vous devez initialiser la base de données à nouveau :

```bash
# Initialize the database
flask --app flaskr init-db
```
