# Realizar un rebase interactivo

Estás trabajando en un proyecto con un equipo de desarrolladores y has realizado varios commits en tu rama. Sin embargo, te das cuenta de que algunos de los commits son innecesarios o deben ser combinados. Quieres limpiar tu historial de commits y hacerlo más organizado.

Para este laboratorio, usemos el repositorio de `https://github.com/labex-labs/git-playground`. Siga estos pasos:

1. Navegue hasta el directorio:
   ```shell
   cd git-playground
   ```
2. Realice un rebase interactivo de los últimos 2 commits:
   ```shell
   git rebase -i HEAD~2
   ```
   El archivo de rebase interactivo se abrirá en tu editor de texto predeterminado. Puedes modificar el orden de los commits y la acción a realizar para cada uno (pick, squash, drop, reword, etc.).
3. Cambie "pick" a "squash" en el mensaje de commit "Added file2.txt", presione <kbd>Esc</kbd> y escriba el comando <kbd>:wq</kbd>, luego presione <kbd>Enter</kbd> para guardar tus cambios y salir del editor, cambie el mensaje de commit a "Added file1.txt and file2.txt" de la misma manera y salga.
4. Si hay conflictos de fusión o necesitas hacer cambios, puedes continuar el rebase cuando estés listo usando `git rebase --continue` o abortarlo usando `git rebase --abort`.

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
