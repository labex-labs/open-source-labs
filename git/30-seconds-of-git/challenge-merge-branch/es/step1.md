# Fusionar una rama

Tu tarea es fusionar una rama en la rama actual utilizando Git. Necesitarás cambiar a la rama destino y luego fusionar la rama origen en ella. Esto puede ser útil cuando quieres combinar los cambios de una rama `feature-branch-A` en la rama `master` de tu proyecto.

## Tareas

Para este desafío, vamos a utilizar el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navega hasta el directorio y configura la identidad.
2. Crea una rama `feature-branch-A`. Cambia a ella.
3. Agrega "hello,world" al archivo `file2.txt`, agréguelo al área de preparación y confírmalo con el mensaje "fix file2.txt".
4. Cambia a la rama `master`.
5. Fusiona la rama `feature-branch-A` en la rama `master`.
6. Resuelve cualquier conflicto que pueda surgir durante el proceso de fusión.

Este es el resultado de ejecutar `git log`:

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <xiaoshengyunan@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
