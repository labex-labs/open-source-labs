# Ejecute su primer contenedor

Vamos a usar la CLI de Docker para ejecutar nuestro primer contenedor.

Abra una terminal en la VM de LabEx.

Ejecute el comando.

```bash
docker container run -t ubuntu top
```

Utilice el comando `docker container run` para ejecutar un contenedor con la imagen `ubuntu` usando el comando `top`. La bandera `-t` asigna un pseudo-TTY que necesitamos para que funcione correctamente `top`.

```bash
$ docker container run -it ubuntu top
No se encuentra la imagen 'ubuntu:latest' localmente
latest: Buscando en el repositorio de Docker Hub
aafe6b5e13de: Descarga completada
0a2b43a72660: Descarga completada
18bdd1e546d2: Descarga completada
8198342c3e05: Descarga completada
f56970a44fd4: Descarga completada
Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
Estado: Imagen actualizada: ubuntu:latest
```

El comando `docker run` primero resultará en un `docker pull` para descargar la imagen de ubuntu en su host. Una vez que se ha descargado, iniciará el contenedor. La salida del contenedor en ejecución debería verse así:

```bash
top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
```

`top` es una utilidad de Linux que imprime los procesos en un sistema y los ordena por consumo de recursos. Observe que solo hay un solo proceso en esta salida: es el propio proceso `top`. No vemos otros procesos de nuestro host en esta lista debido al aislamiento del espacio de nombres PID.

Los contenedores utilizan los espacios de nombres de Linux para proporcionar aislamiento de los recursos del sistema de otros contenedores o del host. El espacio de nombres PID proporciona aislamiento para los identificadores de proceso. Si ejecuta `top` mientras está dentro del contenedor, notará que muestra los procesos dentro del espacio de nombres PID del contenedor, que es muy diferente de lo que puede ver si ejecuta `top` en el host.

Aunque estamos usando la imagen `ubuntu`, es importante destacar que nuestro contenedor no tiene su propio kernel. Utiliza el kernel del host y la imagen `ubuntu` solo se utiliza para proporcionar el sistema de archivos y las herramientas disponibles en un sistema ubuntu.

Inspeccione el contenedor con `docker container exec`

El comando `docker container exec` es una forma de "entrar" en los espacios de nombres de un contenedor en ejecución con un nuevo proceso.

Abra una nueva terminal. Seleccione `Terminal` > `Nueva terminal`.

En la nueva terminal, use el comando `docker container ls` para obtener el ID del contenedor en ejecución que acaba de crear.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
b3ad2a23fab3 ubuntu "top" 29 minutes ago Up 29 minutes goofy_nobel
```

Luego, use ese id para ejecutar `bash` dentro de ese contenedor usando el comando `docker container exec`. Dado que estamos usando bash y queremos interactuar con este contenedor desde nuestra terminal, use las banderas `-it` para ejecutar en modo interactivo mientras asigna un pseudo-terminal.

```bash
$ docker container exec -it ID < CONTAINER > bash
root@b3ad2a23fab3:/#
```

¡Y voilà! Acabamos de usar el comando `docker container exec` para "entrar" en los espacios de nombres de nuestro contenedor con nuestro proceso bash. Usar `docker container exec` con `bash` es un patrón común para inspeccionar un contenedor de Docker.

Observe el cambio en el prefijo de su terminal. Por ejemplo, `root@b3ad2a23fab3:/`. Esto es una indicación de que estamos ejecutando bash "dentro" de nuestro contenedor.

**Nota**: Esto no es lo mismo que conectarse por ssh a un host o una VM separada. No necesitamos un servidor ssh para conectarnos con un proceso bash. Recuerde que los contenedores utilizan características a nivel de kernel para lograr el aislamiento y que los contenedores se ejecutan sobre el kernel. Nuestro contenedor es solo un grupo de procesos que se ejecutan en aislamiento en el mismo host, y podemos usar `docker container exec` para entrar en ese aislamiento con el proceso `bash`. Después de ejecutar `docker container exec`, el grupo de procesos que se ejecutan en aislamiento (es decir, nuestro contenedor) incluye `top` y `bash`.

Desde la misma terminal, ejecute `ps -ef` para inspeccionar los procesos en ejecución.

```bash
root@b3ad2a23fab3:/# ps -ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 20:34? 00:00:00 top
root 17 0 0 21:06? 00:00:00 bash
root 27 17 0 21:14? 00:00:00 ps -ef
```

Debería ver solo el proceso `top`, el proceso `bash` y nuestro proceso `ps`.

Para comparar, salga del contenedor y ejecute `ps -ef` o `top` en el host. Estos comandos funcionarán en Linux o Mac. Para Windows, puede inspeccionar los procesos en ejecución usando `tasklist`.

```bash
root@b3ad2a23fab3:/# exit
exit
$ ps -ef
# Muchos procesos!
```

_Descripción técnica detallada_
PID es solo uno de los espacios de nombres de Linux que proporciona aislamiento a los contenedores de los recursos del sistema. Otros espacios de nombres de Linux incluyen:

- MNT - Montar y desmontar directorios sin afectar a otros espacios de nombres
- NET - Los contenedores tienen su propia pila de red
- IPC - Mecanismos de comunicación interproceso aislados, como colas de mensajes.
- Usuario - Vista aislada de los usuarios en el sistema
- UTC - Establecer el nombre de host y el nombre de dominio por contenedor

Estos espacios de nombres juntos proporcionan el aislamiento para los contenedores que les permite ejecutarse juntos de manera segura y sin conflicto con otros contenedores que se ejecutan en el mismo sistema. A continuación, demostraremos diferentes usos de los contenedores y el beneficio del aislamiento a medida que ejecutamos múltiples contenedores en el mismo host.

**Nota**: Los espacios de nombres son una característica del **kernel** de Linux. Pero Docker le permite ejecutar contenedores en Windows y Mac... ¿cómo funciona eso? El secreto es que integrado en el producto Docker o el motor de Docker hay un subsistema de Linux. Docker abrió este subsistema de Linux a un nuevo proyecto: [LinuxKit](https://github.com/linuxkit/linuxkit). Ser capaz de ejecutar contenedores en muchas plataformas diferentes es una ventaja de usar la herramienta Docker con contenedores.

Además de ejecutar contenedores de Linux en Windows usando un subsistema de Linux, ahora es posible utilizar contenedores nativos de Windows debido a la creación de primitivas de contenedores en el sistema operativo Windows. Los contenedores nativos de Windows se pueden ejecutar en Windows 10 o Windows Server 2016 o versiones posteriores.

**Nota**: si ejecuta este ejercicio en un terminal contenedorizado y ejecuta el comando `ps -ef` en el terminal, todavía verá un conjunto limitado de procesos después de salir del comando `exec`. Puede intentar ejecutar el comando `ps -ef` en un terminal de su máquina local para ver todos los procesos.

Limpie el contenedor que está ejecutando los procesos `top` escribiendo: `<ctrl>-c`, liste todos los contenedores y elimine los contenedores por su id.

```bash
docker ps -a

docker rm <CONTAINER ID>
```
