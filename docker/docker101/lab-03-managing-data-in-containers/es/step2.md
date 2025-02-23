# Montajes Vinculados

La sintaxis `mount` es recomendada por Docker en lugar de la sintaxis `volume`. Los montajes vinculados tienen una funcionalidad limitada en comparación con los volúmenes. Un archivo o directorio se referencia por su ruta completa en la máquina host cuando se monta en un contenedor. Los montajes vinculados dependen de que el sistema de archivos de la máquina host tenga una estructura de directorio específica disponible y no se puede usar la CLI de Docker para administrar los montajes vinculados. Tenga en cuenta que los montajes vinculados pueden cambiar el sistema de archivos host a través de procesos que se ejecutan en un contenedor.

En lugar de usar la sintaxis `-v` con tres campos separados por el separador de dos puntos (:), la sintaxis `mount` es más detallada y utiliza múltiples pares `clave-valor`:

- type: bind, volume o tmpfs,
- source: ruta al archivo o directorio en la máquina host,
- destination: ruta en el contenedor,
- readonly,
- bind-propagation: rprivate, private, rshared, shared, rslave, slave,
- consistency: consistent, delegated, cached,
- mount.

```bash
cd /home/labex/project
mkdir data
docker run -it --name busybox --mount type=bind,source="$(pwd)"/data,target=/data busybox sh
```

Escriba el comando en el contenedor:

```
echo "hello busybox" > /data/hi.txt
exit
```

Verifique que el archivo se haya creado en la máquina host.

```
cat data/hi.txt
```
