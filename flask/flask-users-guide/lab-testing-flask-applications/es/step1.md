# Configurar el entorno de prueba

Antes de poder comenzar a escribir pruebas para su aplicación Flask, debe configurar el entorno de prueba. Aquí están los pasos para hacerlo:

1. Instale el marco `pytest` ejecutando el siguiente comando:

   ```bash
   pip install pytest
   ```

2. Cree un nuevo archivo llamado `conftest.py` en la carpeta `tests` de su aplicación Flask.

3. En el archivo `conftest.py`, importe los módulos necesarios:

   ```python
   import pytest
   from my_app import create_app
   ```

4. Defina un fixture llamado `app` que cree y configure una instancia de la aplicación:

   ```python
   @pytest.fixture()
   def app():
       app = create_app()
       app.config.update({
           "TESTING": True,
       })
       yield app
   ```

   Tenga en cuenta que si está utilizando un patrón de fábrica de aplicaciones, debe modificar el fixture en consecuencia.

5. Defina fixtures para el cliente de prueba y el ejecutor de CLI:

   ```python
   @pytest.fixture()
   def client(app):
       return app.test_client()

   @pytest.fixture()
   def runner(app):
       return app.test_cli_runner()
   ```
