# Ver un resumen corto de los commits sin los commits de fusión

Has estado trabajando en un proyecto con varios otros desarrolladores y quieres ver un resumen de todos los commits realizados en el repositorio. Sin embargo, no quieres ver los commits de fusión, ya que no contienen ningún cambio real en el código. ¿Cómo puedes ver un resumen de todos los commits, excluyendo los commits de fusión?

## Tareas

Para este desafío, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navegue hasta el directorio y configure la identidad.
2. Cree y cambie a una rama llamada `feature1`, cree un archivo llamado `file.txt` y escriba "característica 1" en él, agréguelo al área de preparación y confirme con el mensaje "Agregar característica 1".
3. Vuelva a la rama `master`, una vez fusionada la rama `feature1`, deshabilite la fusión hacia adelante, guarde y salga sin cambiar el texto.
4. Ver un resumen corto de todos los commits, excluyendo los commits de fusión.

Esto generará una lista de todos los commits realizados en el repositorio, excluyendo cualquier commit de fusión. La salida se verá así:

```shell
430b986 (feature1) Agregar característica 1
d22f46b (origin/master, origin/HEAD) Agregado file2.txt
cf80005 Agregado file1.txt
b00b937 Commit inicial
```
