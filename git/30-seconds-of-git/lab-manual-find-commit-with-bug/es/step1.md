# Encontrar manualmente el commit que introdujo un error

Tu tarea es encontrar manualmente el commit que introdujo un error en el repositorio `git-playground`. El repositorio se puede encontrar en `https://github.com/labex-labs/git-playground`. El error es que el archivo `file2.txt` debería imprimir "This is file2.txt." en lugar de "This is file2.".

Para completar este laboratorio, necesitarás usar el comando `git bisect` para realizar una búsqueda binaria a través del historial de commits del repositorio. Necesitarás marcar los commits como "buenos" (sin errores) o "malos" (con errores) hasta que hayas reducido el commit que introdujo el error.

1. Cambia al directorio del repositorio:

```
cd git-playground
```

2. Inicia el proceso de `git bisect`:

```
git bisect start
```

3. Marca el commit actual como "malo":

```
git bisect bad HEAD
```

4. Marca un commit con el mensaje "Initial commit" como "bueno". Git te cambiará automáticamente a un nuevo commit para que lo pruebas:

```
git bisect good 3050fc0de
```

Git te cambiará automáticamente a un nuevo commit para que lo pruebas. 5. Si el contenido del archivo `file2.txt` revisado no coincide con el error, márquelo como "bueno":

```
cat file2.txt
git bisect good
```

6. Si el contenido del archivo `file2.txt` revisado coincide con el error, márquelo como "malo":

```
git bisect bad
```

7. Una vez que hayas encontrado el commit con el error, restablece el proceso de `git bisect`:

```
git bisect reset
```

Ahora puedes examinar los cambios de código en el commit con el error para encontrar la fuente del error.

Este es el resultado de la prueba:

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 is the first bad commit
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
