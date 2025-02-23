# Crear un commit de Git

Has realizado algunos cambios en tu código y quieres guardarlos como una instantánea en tu repositorio de Git. Sin embargo, no quieres guardar todos los cambios que has hecho, solo los que son relevantes para la característica actual o la corrección de errores. ¿Cómo puedes crear un commit que contenga solo los cambios relevantes?

Para este laboratorio, vamos a usar el repositorio de `https://github.com/labex-labs/git-playground`, sigue estos pasos:

1. Clona el repositorio y navega por él:

   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```

2. Configura tu cuenta de github en el entorno:

   ```
   git config --global user.name "tu-nombre"
   git config --global user.email "tu-correo"
   ```

3. Agrega "hello,labex" al archivo `README.md`, agrégalo al área de preparación y confirma con el mensaje "Actualizar README.md":

   ```
   echo "hello,labex" >> README.md
   git add.
   git commit -m "Actualizar README.md"
   ```

   La opción `-m` te permite especificar un mensaje de commit. Asegúrate de que el mensaje sea descriptivo y explique qué cambios contiene el commit.

Este es el resultado de ejecutar el comando `git log`:

![git log command output](../assets/challenge-create-commit-step1-1.png)
