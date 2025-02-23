# Configurar la clave secreta

En un entorno de producción, debes cambiar la clave secreta a un valor aleatorio. Para generar una clave secreta aleatoria, ejecuta el siguiente comando:

```bash
# Genera una clave secreta aleatoria
python -c 'import secrets; print(secrets.token_hex())'
```

Crea un archivo `config.py` en la carpeta de instancia y establece `SECRET_KEY` con el valor generado.

```python
#.venv/var/flaskr-instance/config.py

SECRET_KEY = 'tu_clave_secreta_generada'
```
