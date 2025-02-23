# Comprendiendo las capas de imágenes

Una de las principales propiedades de diseño de Docker es el uso del sistema de archivos union.

Considera el `Dockerfile` que creamos anteriormente:

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py
```

Cada una de estas líneas es una capa. Cada capa contiene solo el delta, la diferencia o los cambios con respecto a las capas anteriores. Para unir estas capas en un solo contenedor en ejecución, Docker utiliza el `sistema de archivos union` para superponer las capas de manera transparente en una sola vista.

Cada capa de la imagen es `de solo lectura`, excepto la última capa, que se crea para el contenedor en ejecución. La capa del contenedor de lectura/escritura implementa "copiar al escribir", lo que significa que los archivos que se almacenan en las capas inferiores de la imagen se copian a la capa del contenedor de lectura/escritura solo cuando se editan esos archivos. Luego, esos cambios se almacenan en la capa del contenedor en ejecución. La función "copiar al escribir" es muy rápida y, en casi todos los casos, no tiene un efecto notable en el rendimiento. Puedes inspeccionar qué archivos se han copiado a nivel de contenedor con el comando `docker diff`. Más información sobre cómo usar `docker diff` se puede encontrar [aquí](https://docs.docker.com/engine/reference/commandline/diff/).

![understanding image layers](../assets/lab2_understanding_image_layers_1.png)

Dado que las capas de imágenes son `de solo lectura`, pueden ser compartidas por imágenes y por contenedores en ejecución. Por ejemplo, crear una nueva aplicación de Python con su propio Dockerfile con capas base similares, compartiría todas las capas que tuviera en común con la primera aplicación de Python.

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app2.py"]
COPY app2.py /app2.py
```

![understanding image layers](../assets/lab2_understanding_image_layers_2.png)

También puedes experimentar la compartición de capas cuando se inician múltiples contenedores a partir de la misma imagen. Dado que los contenedores usan las mismas capas de solo lectura, puedes imaginar que iniciar los contenedores es muy rápido y tiene un impacto muy bajo en el host.

Es posible que note que hay líneas duplicadas en este Dockerfile y en el Dockerfile que creó anteriormente en este laboratorio. Aunque este es un ejemplo muy trivial, puedes extraer las líneas comunes de ambos Dockerfiles a un Dockerfile "base", que luego puedes apuntar desde cada uno de tus Dockerfiles hijos usando el comando `FROM`.

La estratificación de imágenes habilita el mecanismo de caché de Docker para compilaciones y subidas. Por ejemplo, la salida de tu última `docker push` muestra que algunas de las capas de tu imagen ya existen en Docker Hub.

```bash
$ docker push $DOCKERHUB_USERNAME/python-hello-world
```

Para examinar más detenidamente las capas, puedes usar el comando `docker image history` de la imagen de Python que creamos.

```bash
$ docker image history python-hello-world
```

Cada línea representa una capa de la imagen. Notarás que las líneas superiores coinciden con el Dockerfile que creaste, y las líneas inferiores se extraen de la imagen de Python padre. No te preocupes por las etiquetas "\<missing\>". Estas todavía son capas normales; simplemente el sistema de Docker no les ha dado un ID.
