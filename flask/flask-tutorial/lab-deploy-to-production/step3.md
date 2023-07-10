# Configure the Secret Key

In a production environment, you should change the secret key to a random value. To generate a random secret key, run the following command:

```bash
# Generate a random secret key
python -c 'import secrets; print(secrets.token_hex())'
```

Create a `config.py` file in the instance folder and set `SECRET_KEY` to the generated value.

```python
# .venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```
