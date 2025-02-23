# Ejecuta la imagen de Docker

Ahora que has construido la imagen, la puedes ejecutar para comprobar que funciona.

Ejecuta la imagen de Docker

```bash
docker run -p 5001:5000 -d python-hello-world
```

La bandera `-p` mapea un puerto que se ejecuta dentro del contenedor a tu host. En este caso, estamos mapeando la aplicación de Python que se ejecuta en el puerto 5000 dentro del contenedor, al puerto 5001 en tu host. Tenga en cuenta que si el puerto 5001 ya está en uso por otra aplicación en su host, es posible que tenga que reemplazar 5001 con otro valor, como 5002.

Navega a la pestaña **PUERTOS** en la ventana del terminal y haz clic en el enlace para abrir la aplicación en una nueva pestaña del navegador.

![Terminal ports tab link](../assets/20230829-13-59-19-e8dZe3aN.png)

En un terminal, ejecuta `curl localhost:5001`, que devuelve `hello world!`.

Verifica la salida de los registros del contenedor.

Si quieres ver los registros de tu aplicación, puedes usar el comando `docker container logs`. Por defecto, `docker container logs` imprime lo que se envía a la salida estándar por tu aplicación. Utiliza `docker container ls` para encontrar el id de tu contenedor en ejecución.

```bash
labex:project/ $ docker container ls
CONTAINER ID   IMAGE                COMMAND           CREATED         STATUS         PORTS                                       NAMES
52df977e5541   python-hello-world   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, :::5001->5000/tcp   heuristic_lamport
labex:project/ $ docker container logs 52df977e5541
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET /favicon.ico HTTP/1.1" 404 -
```

El Dockerfile es cómo creas construcciones reproducibles para tu aplicación. Un flujo de trabajo común es que tu automatización de CI/CD ejecute `docker image build` como parte de su proceso de compilación. Una vez que se construyen las imágenes, se enviarán a un registro central, donde pueden accederse todos los entornos (como un entorno de prueba) que necesiten ejecutar instancias de esa aplicación. En el siguiente paso, vamos a subir nuestra imagen personalizada al registro público de Docker: el Docker Hub, donde otros desarrolladores y operadores pueden consumirla.
