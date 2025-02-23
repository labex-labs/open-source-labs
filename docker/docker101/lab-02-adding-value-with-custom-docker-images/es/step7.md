# Limpia

Completar este laboratorio genera una serie de contenedores en ejecución en tu host. Limpiemos estos.

Ejecuta `docker container stop [id_del_contenedor]` para cada contenedor que esté en ejecución

Primero, obtén una lista de los contenedores en ejecución usando `docker container ls`.

```bash
$ docker container ls
```

Luego, ejecuta el comando para cada contenedor de la lista.

```bash
$ docker container stop <id_del_contenedor>
```

Elimina los contenedores detenidos

`docker system prune` es un comando muy útil para limpiar tu sistema. Eliminará cualquier contenedor detenido, volúmenes y redes no utilizados, y imágenes sueltas.

```bash
$ docker system prune
ADVERTENCIA! Esto eliminará:
- todos los contenedores detenidos
- todos los volúmenes no utilizados por al menos un contenedor
- todas las redes no utilizadas por al menos un contenedor
- todas las imágenes sueltas
¿Estás seguro de que quieres continuar? [y/N] y
Contenedores eliminados:
0b2ba61df37fb4038d9ae5d145740c63c2c211ae2729fc27dc01b82b5aaafa26

Espacio recuperado en total: 300.3kB
```
