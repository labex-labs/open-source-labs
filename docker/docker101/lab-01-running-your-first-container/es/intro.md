# Introducción

En este laboratorio, ejecutará su primer contenedor Docker.

Los contenedores son simplemente un proceso (o un grupo de procesos) que se ejecuta en aislamiento. El aislamiento se logra a través de los espacios de nombres de Linux, los grupos de control (cgroups), seccomp y SELinux. Tenga en cuenta que los espacios de nombres de Linux y los grupos de control se integran en el núcleo de Linux. Además del propio núcleo de Linux, no hay nada especial en los contenedores.

Lo que hace útil a los contenedores es la herramienta que los rodea. Para estos laboratorios, usaremos Docker, que ha sido una herramienta ampliamente adoptada para usar contenedores para construir aplicaciones. Docker proporciona a los desarrolladores y operadores una interfaz amigable para construir, enviar y ejecutar contenedores en cualquier entorno con un motor de Docker. Debido a que el cliente de Docker requiere un motor de Docker, una alternativa es usar [Podman](https://podman.io/), que es un motor de contenedores sin demonio para desarrollar, administrar y ejecutar contenedores [OCI](https://opencontainers.org/) y es capaz de ejecutar contenedores como root o en modo sin privilegios de root. Por esas razones, recomendamos Podman, pero debido a la adopción, este laboratorio todavía usa Docker.

En la primera parte de este laboratorio, ejecutaremos nuestro primer contenedor y aprenderemos cómo inspeccionarlo. Podremos presenciar el aislamiento de espacios de nombres que adquirimos del núcleo de Linux.

Después de ejecutar nuestro primer contenedor, profundizaremos en otros usos de los contenedores. Puede encontrar muchos ejemplos de estos en la Tienda de Docker, y ejecutaremos varios tipos diferentes de contenedores en el mismo host. Esto nos permitirá ver el beneficio del aislamiento, donde podemos ejecutar múltiples contenedores en el mismo host sin conflictos.

Usaremos algunos comandos de Docker en este laboratorio. Para obtener la documentación completa de los comandos disponibles, consulte la [documentación oficial](https://docs.docker.com/).
