# Eliminar un archivo del último commit

Has agregado un archivo al último commit que no pretendías incluir. Quieres eliminar el archivo del último commit sin cambiar su mensaje.

Para esta práctica, vamos a usar el repositorio de `https://github.com/labex-labs/git-playground`. Supongamos que tienes un repositorio de Git llamado `git-playground` con un archivo llamado `file2.txt` que accidentalmente agregaste al último commit. Estos son los pasos para eliminar el archivo del último commit:

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

2. Utiliza `git rm --cached <archivo>` para eliminar el `<archivo>` especificado del índice:

```shell
git rm --cached file2.txt
```

3. Utiliza `git commit --amend` para actualizar el contenido del último commit, sin cambiar su mensaje:

```shell
git commit --amend --allow-empty
```

Si el commit es un commit vacío después de eliminar el archivo, utiliza `--allow-empty`, de lo contrario, puedes omitirlo.

Después de ejecutar estos comandos, el archivo `file2.txt` se eliminará del último commit sin cambiar su mensaje.

Esto es lo que sucede cuando eliminas `file2.txt` del control de versiones de Git:

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
