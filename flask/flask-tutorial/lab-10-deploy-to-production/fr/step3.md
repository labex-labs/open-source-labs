# Configure the Secret Key

Dans un environnement de production, vous devriez changer la clé secrète en une valeur aléatoire. Pour générer une clé secrète aléatoire, exécutez la commande suivante :

```bash
# Generate a random secret key
python -c 'import secrets; print(secrets.token_hex())'
```

Créez un fichier `config.py` dans le dossier instance et définissez `SECRET_KEY` sur la valeur générée.

```python
#.venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```
