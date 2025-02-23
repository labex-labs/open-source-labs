# Ver un resumen corto de los commits sin los commits de fusión

Has estado trabajando en un proyecto con varios otros desarrolladores y quieres ver un resumen de todos los commits realizados en el repositorio. Sin embargo, no quieres ver los commits de fusión, ya que no contienen ningún cambio real en el código. ¿Cómo puedes ver un resumen de todos los commits, excluyendo los commits de fusión?

Para este laboratorio, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

2. Crea y cambia a una rama llamada `feature1`, crea un archivo llamado `file.txt` y escribe "feature 1" en él, agréguelo al área de preparación y confirma con el mensaje "Agregar característica 1":

```shell
git checkout -b feature1
echo "Feature 1" >> file.txt
git add.
git commit -m "Agregar característica 1"
```

3. Vuelve a la rama `master`, fusiona la rama `feature1`, deshabilita la fusión hacia adelante, guarda y sale sin cambiar el texto:

```shell
git checkout master
git merge --no-ff feature1
```

4. Ver un resumen corto de todos los commits, excluyendo los commits de fusión:

```shell
git log --oneline --no-merges
```

Esto generará una lista de todos los commits realizados en el repositorio, excluyendo cualquier commit de fusión. La salida se verá así:

```shell
430b986 (feature1) Agregar característica 1
d22f46b (origin/master, origin/HEAD) Agregado file2.txt
cf80005 Agregado file1.txt
b00b937 Commit inicial
```
