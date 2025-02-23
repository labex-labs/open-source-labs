# Empezar

Abra una terminal en la VM de LabEx y ejecute `docker -h`, que le mostrará la página de ayuda de la CLI de Docker.

```bash
$ docker -h
La abreviatura de la bandera -h ha sido desaprobada, utilice --help en su lugar

Uso: docker [OPCIONES] COMANDO

Un entorno de ejecución autónomo para contenedores

...

Comandos de gestión:
builder Gestionar compilaciones
config Gestionar configuraciones de Docker
container Gestionar contenedores
engine Gestionar el motor de Docker
image Gestionar imágenes
network Gestionar redes
node Gestionar nodos de Swarm
plugin Gestionar plugins
secret Gestionar secretos de Docker
service Gestionar servicios
stack Gestionar stacks de Docker
swarm Gestionar Swarm
system Gestionar Docker
trust Gestionar la confianza en las imágenes de Docker
volume Gestionar volúmenes
```

La línea de comandos de Docker se puede utilizar para administrar varias características del motor de Docker. En este laboratorio, nos centraremos principalmente en el comando `container`.

Instale `podman` en su VM de LabEx.

```bash
sudo apt-get update
sudo apt-get install podman -y
```

Si se ha instalado `podman`, puede ejecutar el comando alternativo para comparar.

```bash
sudo podman -h
```

Además, puede revisar la versión de su instalación de Docker con `docker version`

```bash
docker version

Cliente:
Versión: 20.10.21
...

Servidor:
Motor:
Versión: 20.10.21
...
```

Nota que Docker instala tanto un `Cliente` como un `Servidor: Motor de Docker`. Por ejemplo, si ejecuta el mismo comando para podman, verá solo una versión de la CLI, porque podman se ejecuta sin demonio y depende de un entorno de ejecución de contenedores compatible con OCI (runc, crun, runv, etc.) para interactuar con el sistema operativo y crear los contenedores en ejecución.

```bash
sudo podman version --events-backend=none
Versión: 3.4.4
Versión de la API: 3.4.4
Versión de Go: go1.17.3
Compilado: Thu Jan 1 08:00:00 1970
Sistema operativo/Arquitectura: linux/amd64
```
