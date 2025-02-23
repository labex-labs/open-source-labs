# Configuración de Flask

Para comenzar con Flask, debes instalarlo y configurar un nuevo proyecto. Sigue las instrucciones siguientes:

1. Instala Flask ejecutando el siguiente comando en tu terminal o línea de comandos:

   ```bash
   pip install flask
   ```

2. Abre un nuevo archivo y guárdalo como `app.py`.

   ```bash
   cd ~/project
   touch app.py
   ```

3. Importa el módulo Flask y crea una instancia de la clase Flask:

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```
