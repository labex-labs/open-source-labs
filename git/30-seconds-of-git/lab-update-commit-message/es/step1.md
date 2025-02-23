# Cambiar el mensaje del último commit

Imagina que acabas de hacer un commit con algunos cambios en tu repositorio de Git, pero te das cuenta de que cometiste un error de tipeo en el mensaje del commit. Quieres corregir el error sin cambiar los cambios reales que hiciste. ¿Cómo puedes hacer esto?

Para demostrar cómo cambiar el mensaje del último commit, vamos a usar el repositorio de `https://github.com/labex-labs/git-playground`. Sigue estos pasos:

1. Clona el repositorio, navega hasta el directorio y configura la identidad:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "tu-nombre-de-usuario"
   git config --global user.email "tu-correo-electrónico"
   ```
2. Corrige el mensaje del commit del último commit para que diga "Corregir el error de red":
   ```
   git commit --amend -m "Corregir el error de red"
   ```
   Esto abrirá tu editor de texto predeterminado donde podrás modificar el mensaje del commit. Guarda y cierra el editor para completar el proceso.
3. Verifica que el mensaje del commit haya sido cambiado:
   ```
   git log --oneline
   ```

Deberías ver el mensaje del commit actualizado en el registro:

```
54b830b (HEAD -> master) Corregir el error de red
cf80005 Agregar file1.txt
b00b937 Commit inicial
```
