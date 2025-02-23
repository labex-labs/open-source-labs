# Ver diferencias en los cambios

Como desarrollador, es posible que desees ver las diferencias entre tus cambios preparados o no preparados y el último commit. Esto es útil cuando quieres revisar tus cambios antes de confirmarlos o cuando quieres ver qué cambios has realizado desde el último commit.

Para demostrar cómo ver las diferencias en los cambios, usaremos el repositorio `git-playground`. Supongamos que has realizado algunos cambios en el archivo `README.md` y quieres ver las diferencias entre tus cambios y el último commit.

1. Abre tu terminal y navega hasta el directorio `git-playground`:

```shell
cd git-playground
```

2. Utiliza el comando `git diff` para ver las diferencias entre tus cambios no preparados y el último commit:

```shell
git diff
```

3. Alternativamente, puedes usar la opción `--staged` para ver las diferencias entre tus cambios preparados y el último commit:

```shell
git diff --staged
```

Este es el resultado de completar el paso 2:

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

Este es el resultado de completar el paso 3:

```
diff --git a/README.md b/README.md
index 0164284..f47591b 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # git-playground
 Git Playground
+hello,world
```
