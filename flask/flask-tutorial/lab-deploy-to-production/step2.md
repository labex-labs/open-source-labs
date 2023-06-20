# Configure the Secret Key

It's important to change the default value of the `SECRET_KEY` in production to enhance security. Follow the steps below to configure the secret key:

1. Generate a random secret key by running the following command:

```bash
$ python -c 'import secrets; print(secrets.token_hex())'
```

Example output: `'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'`

2. Create the `config.py` file in the instance folder and copy the generated secret key into it:

```python
# .venv/var/flaskr-instance/config.py

SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

You can also set any other necessary configuration in this file.
