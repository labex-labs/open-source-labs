# [Opcional] OverlayFS

OverlayFS es una implementación de `sistema de archivos de montaje union` para Linux. Para entender qué es un volumen de Docker, ayuda entender cómo funcionan las capas y el sistema de archivos en Docker.

Para iniciar un contenedor, Docker toma la imagen de solo lectura y crea una nueva capa de lectura-escritura encima. Para ver las capas como una sola, Docker utiliza un Sistema de Archivos Union o OverlayFS (Sistema de Archivos Superpuesto), específicamente el controlador de almacenamiento `overlay2`.

Para ver los archivos administrados por el host de Docker, necesita acceder al sistema de archivos del proceso de Docker. Usando las banderas `--privileged` y `--pid=host` puede acceder al espacio de nombres de identificadores de proceso del host desde dentro de un contenedor como `busybox`. Luego puede navegar al directorio `/var/lib/docker/overlay2` de Docker para ver las capas descargadas que son administradas por Docker.

Para ver la lista actual de capas en Docker:

```bash
$ docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh

/ # ls -l /var/lib/docker/overlay2
total 16
drwx------ 3 root root 4096 Sep 25 19:44 0e55ecaa4d17c353191e68022d9a17fde64fb5e9217b07b5c56eb4c74dad5b32
drwx------ 5 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d
drwx------ 4 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d-init
drwx------ 2 root root 4096 Sep 25 19:44 l

/ # exit
```

Descargue la imagen `ubuntu` y verifique nuevamente:

```bash
docker pull ubuntu
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
```

Escriba el comando para ver la lista de capas nuevamente:

```
ls -l /var/lib/docker/overlay2/ & exit
```

Verá que al descargar la imagen `ubuntu`, se descargaron implícitamente 4 nuevas capas:

- a611792b4cac502995fa88a888261dfba0b5d852e72f9db9e075050991423779
- d181f1a41fc35a45c16e8bfcb8eee6f768f3b98f82210a43ea65f284a45fcd65
- dac2f37f6280a076836d39b87b0ae5ebf5c0d386b6d8b991b103aadbcebaa7c6
- f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709

El controlador de almacenamiento `overlay2` esencialmente superpone diferentes directorios en el host y los presenta como un solo directorio.

- capa base o lowerdir,
- capa `diff` o upperdir,
- capa superpuesta (vista del usuario), y
- directorio `work`.

OverlayFS se refiere a los directorios inferiores como `lowerdir`, que contiene la imagen base y las capas de solo lectura (R/O) que se descargan.

El directorio superior se llama `upperdir` y es la capa de contenedor de lectura-escritura (R/W).

La vista unificada o capa `overlay` se llama `merged`.

Finalmente, un `workdir` es obligatorio, que es un directorio vacío utilizado por overlay para su uso interno.

El controlador `overlay2` admite hasta 128 capas inferiores de OverlayFS. El directorio `l` contiene identificadores de capa acortados como enlaces simbólicos.

![Controlador de almacenamiento Overlay2](../assets/overlay2-driver.png)

Limpie:

```bash
docker system prune -a
clear
```
