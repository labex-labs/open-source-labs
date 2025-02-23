# Cambiar la URL remota

Has clonado un repositorio de GitHub y has realizado algunos cambios en él. Sin embargo, ahora te das cuenta de que necesitas cambiar la URL del repositorio remoto. Esto podría ser porque el repositorio original ha sido movido a una ubicación diferente, o porque quieres empujar tus cambios a un repositorio remoto diferente. Tu tarea es cambiar la URL remota del repositorio usando comandos de Git.

Necesitarás clonar el repositorio `https://github.com/labex-labs/git-playground` en tu máquina local. Para cambiar la URL remota del repositorio a `https://github.com/your-username/git-playground`, sigue estos pasos:

1. Abre una terminal o línea de comandos, clona el repositorio y navega hasta el repositorio local.
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. Utiliza el siguiente comando para ver la URL remota actual:
   ```
   git remote -v
   ```
3. Utiliza el siguiente comando para cambiar la URL remota a la nueva URL:
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. Utiliza el siguiente comando para verificar que la URL remota ha sido cambiada:
   ```
   git remote -v
   ```

La salida debe mostrar la nueva URL en lugar de la antigua:

![Updated remote URL output](../assets/challenge-change-remote-url-step1-1.png)
