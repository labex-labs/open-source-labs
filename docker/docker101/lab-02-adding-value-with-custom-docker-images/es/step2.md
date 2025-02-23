# Crea y construye la imagen de Docker

Ahora, ¿y si no tienes Python instalado localmente? ¡No te preocupes! Porque no lo necesitas. Una de las ventajas de usar contenedores es que puedes instalar Python dentro de tus contenedores, sin tener que instalar Python en tu máquina host.

Crea un `Dockerfile` ejecutando el siguiente comando. (Copiar y pegar todo el bloque de código)

```bash
echo 'FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py' > Dockerfile
```

Un Dockerfile enumera las instrucciones necesarias para construir una imagen de Docker. Vamos a revisar el archivo anterior línea por línea.

**FROM python:3.8-alpine**
Este es el punto de partida de tu Dockerfile. Todo Dockerfile debe comenzar con una línea `FROM` que es la imagen base sobre la cual se construirán tus capas.

En este caso, estamos seleccionando la capa base `python:3.8-alpine` (ver [Dockerfile para python3.8/alpine3.12](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)) ya que ya tiene la versión de Python y pip que necesitamos para ejecutar nuestra aplicación.

La versión `alpine` significa que utiliza la distribución [Alpine Linux](https://en.wikipedia.org/wiki/Alpine_Linux), que es significativamente más pequeña que muchas otras versiones de Linux alternativas, alrededor de 8 MB de tamaño, mientras que una instalación mínima en disco podría ser de alrededor de 130 MB. Una imagen más pequeña significa que se descargará (desplegará) mucho más rápido, y también tiene ventajas en seguridad porque tiene una superficie de ataque más pequeña. [Alpine Linux](https://alpinelinux.org/downloads/) es una distribución de Linux basada en musl y BusyBox.

Aquí estamos usando la etiqueta "3.8-alpine" para la imagen de Python. Echa un vistazo a las etiquetas disponibles para la imagen oficial de Python en el [Docker Hub](https://hub.docker.com/_/python/). Es una buena práctica usar una etiqueta específica cuando se hereda una imagen padre para controlar los cambios en la dependencia padre. Si no se especifica una etiqueta, la etiqueta "latest" entrará en vigor, que actúa como un puntero dinámico que apunta a la última versión de una imagen.

Por razones de seguridad, es muy importante entender las capas sobre las que se construye tu imagen de Docker. Por eso, se recomienda encarecidamente usar solo imágenes "oficiales" encontradas en el [docker hub](https://hub.docker.com/), o imágenes no comunitarias encontradas en el docker-store. Estas imágenes son [revisadas](https://docs.docker.com/docker-hub/official_repos/) para cumplir ciertos requisitos de seguridad, y también tienen una muy buena documentación para que los usuarios la sigan. Puedes encontrar más información sobre esta [imagen base de Python](https://hub.docker.com/_/python), así como todas las otras imágenes que puedes usar, en el [docker hub](https://hub.docker.com).

Para una aplicación más compleja, es posible que necesites usar una imagen `FROM` que esté más arriba en la cadena. Por ejemplo, el [Dockerfile](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) padre de nuestra aplicación de Python comienza con `FROM alpine`, luego especifica una serie de comandos `CMD` y `RUN` para la imagen. Si necesitabas un control más detallado, podrías comenzar con `FROM alpine` (o una distribución diferente) y ejecutar esos pasos tú mismo. Para empezar, sin embargo, recomiendo usar una imagen oficial que se ajuste a tus necesidades.

**RUN pip install flask**
El comando `RUN` ejecuta los comandos necesarios para configurar tu imagen para tu aplicación, como instalar paquetes, editar archivos o cambiar permisos de archivos. En este caso estamos instalando flask. Los comandos `RUN` se ejecutan durante la construcción y se agregan a las capas de tu imagen.

**CMD ["python","app.py"]**
`CMD` es el comando que se ejecuta cuando se inicia un contenedor. Aquí estamos usando `CMD` para ejecutar nuestra aplicación de Python.

Pueden haber solo un `CMD` por Dockerfile. Si se especifican más de un `CMD`, entonces el último `CMD` entrará en vigor. La imagen padre python:3.8-alpine también especifica un `CMD` (`CMD python3`). Puedes encontrar el Dockerfile para la imagen oficial python:alpine [aquí](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile).

Puedes usar la imagen oficial de Python directamente para ejecutar scripts de Python sin instalar Python en tu host. Pero hoy, estamos creando una imagen personalizada para incluir nuestro código fuente, para que podamos construir una imagen con nuestra aplicación y enviarla a otros entornos.

**COPY app.py /app.py**
Esto copia el app.py en el directorio local (donde ejecutarás `docker image build`) en una nueva capa de la imagen. Esta instrucción es la última línea en el Dockerfile. Las capas que cambian con frecuencia, como copiar el código fuente en la imagen, deben ubicarse cerca del final del archivo para aprovechar al máximo la memoria caché de las capas de Docker. Esto nos permite evitar la reconstrucción de capas que de otra manera podrían estar en caché. Por ejemplo, si hubiera un cambio en la instrucción `FROM`, invalidaría la memoria caché para todas las capas subsiguientes de esta imagen. Lo demostraremos un poco más adelante en este laboratorio.

Parece contraintuitivo poner esto después de la línea `CMD ["python","app.py"]`. Recuerda, la línea `CMD` se ejecuta solo cuando se inicia el contenedor, por lo que no obtendremos un error de `archivo no encontrado` aquí.

Y ahí lo tienes: un Dockerfile muy simple. Una lista completa de comandos que puedes poner en un Dockerfile se puede encontrar [aquí](https://docs.docker.com/engine/reference/builder/). Ahora que definimos nuestro Dockerfile, usémoslo para construir nuestra imagen personalizada de Docker.

Construye la imagen de Docker.

Pasa `-t` para nombrar tu imagen `python-hello-world`.

```bash
docker image build -t python-hello-world.
```

Verifica que tu imagen aparezca en tu lista de imágenes.

```bash
docker image ls
```

**Nota** que tu imagen base `python:3.8-alpine` también está en tu lista.

Puedes ejecutar un comando de historial para mostrar el historial de una imagen y sus capas,

```bash
docker history python-hello-world
docker history python:3.8-alpine
```
