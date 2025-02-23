# Eliminar un archivo del historial

Supongamos que accidentalmente has cometido un archivo que contiene información sensible, como claves de API o contraseñas, en tu repositorio de Git. Te das cuenta de que este archivo nunca debió haber sido cometido y quieres eliminarlo completamente del historial del repositorio. Sin embargo, simplemente eliminar el archivo y cometer el cambio no lo eliminará del historial del repositorio. El archivo todavía será accesible en commits anteriores, lo que podría representar un riesgo de seguridad.

Para completar esta práctica, usarás el repositorio de Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`. Este repositorio contiene un archivo llamado `file1.txt` que nunca debió haber sido cometido. Para eliminar `file1.txt` del historial del repositorio, sigue estos pasos:

1. Clona el repositorio en tu máquina local:

```shell
git clone https://github.com/your-username/git-playground
```

2. Usa los siguientes comandos para navegar al directorio y configurar la identidad:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Elimina el archivo del índice del repositorio.

```shell
git rm --cached --ignore-unmatch file1.txt
```

4. Comete este cambio con el mensaje de commit "Eliminar archivo sensible file1.txt":

```shell
git commit -m "Eliminar archivo sensible file1.txt"
```

5. Reescribe el historial del repositorio, eliminando todas las instancias de `file1.txt`:

```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
```

6. Empuja las modificaciones con fuerza al repositorio remoto:

```shell
git push origin --force --all
```

Después de completar estos pasos, `file1.txt` se eliminará completamente del historial del repositorio y después de ejecutar `git log --remotes`, no verás el commit en `file1.txt`.
