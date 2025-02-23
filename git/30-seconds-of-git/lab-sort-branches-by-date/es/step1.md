# Ordenar ramas de Git por fecha

Tienes un repositorio de Git con múltiples ramas y quieres ordenarlas por fecha. Esto te permitirá ver qué ramas se han actualizado recientemente y cuáles no. Ordenar las ramas por fecha también puede ayudarte a identificar las ramas que pueden necesitar atención o fusión.

Para este laboratorio, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Clona el repositorio en tu máquina local:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Navega hasta el directorio del repositorio y configura tu identidad de GitHub:

```shell
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

3. Crea una rama llamada `one`, modifica el código y confirma los cambios:

```shell
git checkout -b one
touch hello.txt
git add.
git commit -m "hello.txt"
```

4. Cambia a la rama llamada `master` y crea una rama llamada `two`:

```shell
git checkout master
git checkout -b two
```

5. Ahora, para ordenar las ramas por fecha, usa el siguiente comando:

```shell
git branch --sort=-committerdate
```

Esto mostrará una lista de todas las ramas locales y las ordenará según la fecha de su último commit. Puedes usar las flechas para navegar por la lista y presionar <kbd>Q</kbd> para salir.

Este es el resultado final:

![sorted git branches list](../assets/challenge-sort-branches-by-date.png)
