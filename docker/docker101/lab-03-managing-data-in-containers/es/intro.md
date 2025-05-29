# Introducción

Por defecto, todos los archivos creados dentro de un contenedor se almacenan en una capa de contenedor escribible. Eso significa que:

- Si el contenedor ya no existe, los datos se pierden.
- La capa escribible del contenedor está estrechamente acoplada a la máquina host.
- Para administrar el sistema de archivos, se necesita un controlador de almacenamiento que proporcione un sistema de archivos union, utilizando el kernel de Linux. Esta abstracción adicional reduce el rendimiento en comparación con los `volúmenes de datos`, que escriben directamente en el sistema de archivos.

Docker ofrece dos opciones para almacenar archivos en la máquina host: `volúmenes` y `montajes vinculados`. Si estás ejecutando Docker en Linux, también puedes usar un `montaje tmpfs`, y con Docker en Windows también puedes usar un `tuberia con nombre`.

![Tipos de Montajes](../assets/types-of-mounts.png)

- Los `volúmenes` se almacenan en el sistema de archivos host administrado por Docker.
- Los `montajes vinculados` se almacenan en cualquier lugar del sistema host.
- Los `montajes tmpfs` se almacenan solo en la memoria host.

Originalmente, la bandera `--mount` se utilizaba para los servicios de Docker Swarm y la bandera `--volume` se utilizaba para contenedores independientes. A partir de Docker 17.06 y versiones superiores, también puedes usar `--mount` para contenedores independientes y, en general, es más explícito y detallado que `--volume`.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Este es un Guided Lab, que proporciona instrucciones paso a paso para ayudarte a aprender y practicar. Sigue las instrucciones cuidadosamente para completar cada paso y obtener experiencia práctica. Los datos históricos muestran que este es un laboratorio de nivel <span class="text-green-600 dark:text-green-400">principiante</span> con una tasa de finalización del <span class="text-green-600 dark:text-green-400">100%</span>. Ha recibido una tasa de reseñas positivas del <span class="text-primary-600 dark:text-primary-400">100%</span> por parte de los estudiantes.
</div>
