# Escribir pruebas

Ahora que ha configurado el entorno de prueba, puede comenzar a escribir pruebas para su aplicación Flask. Aquí hay algunos ejemplos de pruebas comunes que puede desear escribir:

1. Probar una ruta:

   ```python
   def test_hello(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, World!" in response.data
   ```

   Esta prueba envía una solicitud GET a la ruta raíz ("/") y comprueba que el código de estado de la respuesta sea 200 y que los datos de la respuesta contengan la cadena "Hello, World!".

2. Probar una solicitud POST:

   ```python
   def test_login(client):
       response = client.post("/login", data={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert b"Logged in successfully" in response.data
   ```

   Esta prueba envía una solicitud POST a la ruta de inicio de sesión ("/login") con datos del formulario que contienen un nombre de usuario y una contraseña. Comprueba que el código de estado de la respuesta sea 200 y que los datos de la respuesta contengan la cadena "Logged in successfully".

3. Probar un comando:

   ```python
   def test_hello_command(runner):
       result = runner.invoke(args=["hello"])
       assert result.exit_code == 0
       assert "Hello, World!" in result.output
   ```

   Esta prueba invoca un comando llamado "hello" y comprueba que el comando salga con un código de 0 y que la salida contenga la cadena "Hello, World!".
