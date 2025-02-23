# Limpie

Completar este laboratorio resulta en una serie de contenedores en ejecución en su host. Limpiemos estos.

Primero, obtenga una lista de los contenedores en ejecución usando `docker container ls`.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." 3 minutos atrás En ejecución hace 3 minutos 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 3 minutos atrás En ejecución hace 3 minutos 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 8 minutos atrás En ejecución hace 8 minutos priceless_kepler
```

Luego, ejecute `docker container stop [container id]` para cada contenedor de la lista. También puede usar los nombres de los contenedores que especificó anteriormente.

```bash
$ docker container stop d67 ead af5
d67
ead
af5
```

**Nota**: Solo tiene que referirse a suficientes dígitos del ID para que sea único. Tres dígitos casi siempre son suficientes.

Elimine los contenedores detenidos

`docker system prune` es un comando muy útil para limpiar su sistema. Eliminará cualquier contenedor detenido, volúmenes y redes no utilizados y imágenes sueltas.

```bash
$ docker system prune
ADVERTENCIA! Esto eliminará:
- todos los contenedores detenidos
- todos los volúmenes no utilizados por al menos un contenedor
- todas las redes no utilizadas por al menos un contenedor
- todas las imágenes sueltas
¿Está seguro de que desea continuar? [y/N] y
Contenedores eliminados:
7872fd96ea4695795c41150a06067d605f69702dbcb9ce49492c9029f0e1b44b
60abd5ee65b1e2732ddc02b971a86e22de1c1c446dab165462a08b037ef7835c
31617fdd8e5f584c51ce182757e24a1c9620257027665c20be75aa3ab6591740

Espacio recuperado en total: 12B
```
