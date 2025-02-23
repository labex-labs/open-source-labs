# Ejecute múltiples contenedores

## Explore el Docker Hub

El [Docker Hub](https://hub.docker.com/explore/) es el registro central público de imágenes de Docker, que contiene imágenes comunitarias y oficiales.

Al buscar imágenes, encontrará filtros para "Certificados por Docker", "Editor Verificado" e "Imágenes Oficiales". Seleccione el filtro "Certificados por Docker" para encontrar imágenes que se consideran aptas para la empresa y que se han probado con el producto Docker Enterprise Edition. Es importante evitar usar contenido no verificado de la Tienda de Docker al desarrollar sus propias imágenes destinadas a ser desplegadas en el entorno de producción. Estas imágenes no verificadas pueden contener vulnerabilidades de seguridad o incluso software malicioso.

En el paso 2 de este laboratorio, iniciaremos varios contenedores usando algunas imágenes verificadas del Docker Hub: el servidor web nginx y la base de datos mongo.

## Ejecute un servidor Nginx

Vamos a ejecutar un contenedor usando la [imagen oficial de Nginx](https://hub.docker.com/_/nginx) del Docker Hub.

```bash
docker container run --detach --publish 8080:80 --name nginx nginx
```

Estamos usando un par de nuevas banderas aquí. La bandera `--detach` ejecutará este contenedor en segundo plano. La bandera `publish` publica el puerto 80 en el contenedor (el puerto predeterminado para nginx), a través del puerto 8080 en nuestro host. Recuerde que el espacio de nombres NET da a los procesos del contenedor su propia pila de red. La bandera `--publish` es una característica que nos permite exponer la red a través del contenedor hacia el host.

¿Cómo sabe que el puerto 80 es el puerto predeterminado para nginx? Porque está listado en la [documentación](https://hub.docker.com/_/nginx) del Docker Hub. En general, la documentación de las imágenes verificadas es muy buena, y la tendrá en cuenta cuando ejecute contenedores usando esas imágenes.

También estamos especificando la bandera `--name`, que nombra el contenedor. Cada contenedor tiene un nombre, si no lo especifica, Docker le asignará uno aleatoriamente. Especificar su propio nombre facilita la ejecución de comandos posteriores en su contenedor, ya que puede hacer referencia al nombre en lugar del id del contenedor. Por ejemplo: `docker container inspect nginx` en lugar de `docker container inspect 5e1`.

Dado que esta es la primera vez que ejecuta el contenedor nginx, descargará la imagen nginx de la Tienda de Docker. Los contenedores posteriores creados a partir de la imagen de Nginx usarán la imagen existente ubicada en su host.

Nginx es un servidor web ligero. Puede acceder al servidor nginx en la pestaña **Web 8080** de la VM de LabEx. Cambie a ella y actualice la página para ver la salida de nginx.

![step 2 nginx](../assets/20230829-11-16-04-BazUogDa.png)

## Ejecute un servidor de base de datos `mongo`

Ahora, ejecute un servidor de base de datos mongo. Usaremos la [imagen oficial de mongoDB](https://hub.docker.com/_/mongo) del Docker Hub. En lugar de usar la etiqueta `latest` (que es la predeterminada si no se especifica una etiqueta), usaremos una versión específica de la imagen de mongo: 4.4.

```bash
docker container run --detach --publish 8081:27017 --name mongo mongo:4.4
```

Nuevamente, dado que esta es la primera vez que ejecutamos un contenedor de mongo, descargaremos la imagen de mongo de la Tienda de Docker. Estamos usando la bandera `--publish` para exponer el puerto 27017 de mongo en nuestro host. Tenemos que usar un puerto diferente de 8080 para el mapeo del host, ya que ese puerto ya está expuesto en nuestro host. Vuelva a consultar la [documentación oficial](https://hub.docker.com/_/mongo) del Docker Hub para obtener más detalles sobre el uso de la imagen de mongo.

Vea la salida de mongoDB usando `0.0.0.0:8081` en el navegador web. Debería ver un mensaje que devolverá una advertencia de MongoDB.

![MongoDB server output warning](../assets/20230829-11-19-23-PkodKK48.png)

Verifique sus contenedores en ejecución con `docker container ls`

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." Menos de un segundo atrás En ejecución hace 2 segundos 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." Hace 17 segundos En ejecución hace 19 segundos 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" Hace 5 minutos En ejecución hace 5 minutos priceless_kepler
```

Debería ver que tiene un contenedor de servidor web Nginx y un contenedor de MongoDB en ejecución en su host. Tenga en cuenta que no hemos configurado estos contenedores para que se comuniquen entre sí.

Puede ver los nombres "nginx" y "mongo" que le dimos a nuestros contenedores, y el nombre aleatorio (en mi caso "priceless_kepler") que se generó para el contenedor ubuntu. También puede ver los mapeos de puerto que especificamos con la bandera `--publish`. Para obtener más detalles sobre estos contenedores en ejecución, puede usar el comando `docker container inspect [container id`.

Una cosa que puede notar es que el contenedor de mongo está ejecutando el comando `docker-entrypoint`. Este es el nombre del ejecutable que se ejecuta cuando se inicia el contenedor. La imagen de mongo requiere alguna configuración previa antes de iniciar el proceso de base de datos. Puede ver exactamente lo que hace el script mirándolo en [github](https://github.com/docker-library/mongo). Por lo general, puede encontrar el enlace al código fuente de github desde la página de descripción de la imagen en el sitio web de la Tienda de Docker.

Los contenedores son autónomos e aislados, lo que significa que podemos evitar posibles conflictos entre contenedores con diferentes dependencias de sistema o tiempo de ejecución. Por ejemplo: desplegar una aplicación que utiliza Java 7 y otra aplicación que utiliza Java 8 en el mismo host. O ejecutar múltiples contenedores de nginx que todos tienen el puerto 80 como sus puertos de escucha predeterminados (si se expone en el host usando la bandera `--publish`, los puertos seleccionados para el host deben ser únicos). Los beneficios del aislamiento son posibles gracias a los espacios de nombres de Linux.

**Nota**: No tuvo que instalar nada en su host (aparte de Docker) para ejecutar estos procesos. Cada contenedor incluye las dependencias que necesita dentro del contenedor, por lo que no necesita instalar nada directamente en su host.

Ejecutar múltiples contenedores en el mismo host nos da la capacidad de utilizar al máximo los recursos (cpu, memoria, etc.) disponibles en un solo host. Esto puede resultar en grandes economías de costos para una empresa.

Si bien ejecutar imágenes directamente del Docker Hub puede ser útil en ocasiones, es más útil crear imágenes personalizadas y referirse a las imágenes oficiales como punto de partida para estas imágenes. Profundizaremos en la creación de nuestras propias imágenes personalizadas en el Laboratorio 2.
