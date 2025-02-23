# Realizar un rebase interactivo

Estás trabajando en un proyecto con un equipo de desarrolladores y has realizado varios commits en tu rama. Sin embargo, te das cuenta de que algunos de los commits son innecesarios o deben ser combinados. Quieres limpiar tu historial de commits y hacerlo más organizado.

## Tareas

Para este desafío, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navega hasta el directorio.
2. Realiza un rebase interactivo de los últimos 2 commits.
3. Cambia "pick" a "squash" en el mensaje de commit "Added file2.txt", presiona <kbd>Esc</kbd> y escribe el comando <kbd>:wq</kbd>, luego presiona <kbd>Enter</kbd> para guardar tus cambios y salir del editor, cambia el mensaje de commit a "Added file1.txt and file2.txt" de la misma manera y sale.

Ejecutar `git log` te dará un resultado que se parece a esto:

```shell
commit 7575ded485555c28ecb09487c68e90639bebbe9d (HEAD -> master)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt and file2.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
