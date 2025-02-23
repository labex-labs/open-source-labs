# Fusionar una rama

Tu tarea es fusionar una rama en la rama actual utilizando Git. Necesitarás cambiar a la rama destino y luego fusionar la rama origen en ella. Esto puede ser útil cuando quieres combinar los cambios de una rama `feature-branch-A` en la rama `master` de tu proyecto.

Para este laboratorio, vamos a utilizar el repositorio de `https://github.com/labex-labs/git-playground`. Sigue estos pasos para fusionar la rama `feature-branch-A` en la rama `master`:

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

2. Crea una rama `feature-branch-A`. Cambia a ella:

```shell
git checkout -b feature-branch-A
```

3. Agrega "hello,world" al archivo `file2.txt`, agréguelo al área de preparación y confírmalo con el mensaje "arreglar file2.txt":

```shell
echo "hello,world" >> file2.txt
git add.
git commit -m "arreglar file2.txt"
```

4. Cambia a la rama `master`:

```shell
git checkout master
```

5. Fusiona la rama `feature-branch-A` en la rama `master`:

```shell
git merge feature-branch-A
```

6. Resuelve cualquier conflicto que pueda surgir durante el proceso de fusión.

Este es el resultado de ejecutar `git log`:

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    arreglar file2.txt
```
