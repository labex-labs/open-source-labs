# Volver a la Rama Anterior

Como desarrollador, estás trabajando en un proyecto y has cambiado a una rama diferente para trabajar en una nueva característica. Después de realizar algunos cambios, te das cuenta de que necesitas cambiar de nuevo a la rama anterior para corregir un error. Puedes confirmar tus cambios en una nueva rama y usar un comando para cambiar rápidamente a la rama anterior.

Para demostrar cómo cambiar de nuevo a la rama anterior, usaremos el repositorio de Git llamado `https://github.com/labex-labs/git-playground`. Siga los pasos siguientes:

1. Clone el repositorio usando el siguiente comando:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Cambie al directorio del repositorio:
   ```
   cd git-playground
   ```
3. Cree una nueva rama llamada `feature-branch`:
   ```
   git checkout -b feature-branch
   ```
4. Verifique la rama actual y cambie rápidamente a la rama anterior. El nombre de su nueva rama es `feature-branch` y el nombre de la rama anterior a la que desea cambiar de nuevo es `master`:
   ```
   git checkout -
   ```
   Esto cambiará de nuevo a la rama `master`, y tus cambios todavía estarán allí.
