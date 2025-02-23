# Eliminar un archivo del historial

Supongamos que accidentalmente has hecho commit de un archivo que contiene información sensible, como claves de API o contraseñas, en tu repositorio de Git. Te das cuenta de que este archivo nunca debió haber sido hecho commit y quieres eliminarlo completamente del historial del repositorio. Sin embargo, simplemente eliminar el archivo y hacer commit del cambio no lo eliminará del historial del repositorio. El archivo todavía será accesible en commits anteriores, lo que podría representar un riesgo de seguridad.

## Tareas

Para completar este desafío, usarás el repositorio de Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`. Este repositorio contiene un archivo llamado `file1.txt` que nunca debió haber sido hecho commit. Por favor, elimina `file1.txt` del historial del repositorio.

1. Clona el repositorio en tu máquina local desde `https://github.com/your-username/git-playground`.
2. Navega hasta el directorio y configura la identidad.
3. Elimina el archivo del índice del repositorio.
4. Reescribe el historial del repositorio, eliminando todas las instancias de `file1.txt`.
5. Forza el envío de los cambios al repositorio remoto.

Después de completar estos pasos, `file1.txt` se eliminará completamente del historial del repositorio y después de ejecutar `git log --remotes`, no verás el commit en `file1.txt`.
