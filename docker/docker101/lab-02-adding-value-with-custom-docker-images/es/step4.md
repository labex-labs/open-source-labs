# Sube a un registro central

Navega a [Docker Hub](https://hub.docker.com) y crea una cuenta si aún no la tienes. Alternativamente, también puedes usar [https://quay.io](https://quay.io), por ejemplo.

Para este laboratorio, usaremos Docker Hub como nuestro registro central. Docker Hub es un servicio gratuito para almacenar imágenes disponibles públicamente, o puedes pagar para almacenar imágenes privadas. Ve a la página web de [Docker Hub](https://hub.docker.com) y crea una cuenta gratuita.

La mayoría de las organizaciones que usan Docker intensivamente establecerán su propio registro internamente. Para simplificar las cosas, usaremos Docker Hub, pero los siguientes conceptos se aplican a cualquier registro.

Inicia sesión

Puedes iniciar sesión en la cuenta del registro de imágenes escribiendo `docker login` en tu terminal, o si estás usando podman, escribe `podman login`.

```bash
labex:project/ $ export DOCKERHUB_USERNAME=<tu_nombre_de_usuario_de_docker>
labex:project/ $ docker login docker.io -u $DOCKERHUB_USERNAME
Contraseña:
ADVERTENCIA: Tu contraseña se almacenará sin encriptar en /home/labex/.docker/config.json.
Configura un ayudante de credenciales para quitar esta advertencia. Ver
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Inicio de sesión exitoso
```

Etiqueta tu imagen con tu nombre de usuario

La convención de nombres de Docker Hub es etiquetar tu imagen con [nombre de usuario de dockerhub]/[nombre de imagen]. Para hacer esto, vamos a etiquetar nuestra imagen previamente creada `python-hello-world` para que se ajuste a ese formato.

```bash
docker tag python-hello-world $DOCKERHUB_USERNAME/python-hello-world
```

Sube tu imagen al registro

Una vez que tenemos una imagen correctamente etiquetada, podemos usar el comando `docker push` para subir nuestra imagen al registro de Docker Hub.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

Mira tu imagen en Docker Hub en tu navegador

Navega a [Docker Hub](https://hub.docker.com) y ve a tu perfil para ver tu imagen recién subida en `https://hub.docker.com/repository/docker/<nombre_de_usuario_de_dockerhub>/python-hello-world`.

Ahora que tu imagen está en Docker Hub, otros desarrolladores y operaciones pueden usar el comando `docker pull` para desplegar tu imagen en otros entornos.

**Nota**: Las imágenes de Docker contienen todas las dependencias que necesita para ejecutar una aplicación dentro de la imagen. Esto es útil porque ya no tenemos que preocuparnos por la deriva del entorno (diferencias de versión) cuando dependemos de dependencias que se instalan en cada entorno al que desplegamos. Tampoco tenemos que pasar por pasos adicionales para aprovisionar estos entornos. Solo un paso: instala Docker, y ya estás listo.
