# Crear un commit de corrección

Supongamos que estás trabajando en un proyecto con varios otros desarrolladores y notas un pequeño error en un commit que se hizo hace unos días. Quieres corregir el error, pero no quieres crear un nuevo commit y interrumpir el trabajo de los otros desarrolladores. Aquí es donde los commits de corrección resultan útiles. Al crear un commit de corrección, puedes hacer los cambios necesarios sin crear un nuevo commit, y el commit de corrección se fusionará automáticamente con el commit original durante la próxima rebase.

## Tareas

Tu tarea es escribir la cadena "hello,world" en el archivo `hello.txt` y agregarlo como un commit de "corrección" al commit con el mensaje "Added file1.txt", de modo que se pueda fusionar automáticamente en una operación de rebase subsiguiente.

Para este desafío, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navega hasta el directorio y configura la identidad.
2. Crea un archivo `hello.txt`, escribe "hello,world" en él y agréguelo al área de preparación.
3. Crea un commit de corrección para el hash del mensaje de commit "Added file1.txt".
4. Una vez que hayas creado el commit de corrección, puedes fusionar automáticamente el commit de corrección con el commit original durante la próxima rebase. Cuando abres el editor interactivo, no es necesario cambiar el texto y guardar para salir.

Este es el resultado de ejecutar el comando `git show HEAD~1`:

```shell
commit 6f0b8bbfac939af197a44ecd287ef84153817e9d
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

diff --git a/file1.txt b/file1.txt
new file mode 100644
index 0000000..bfccc4a
--- /dev/null
+++ b/file1.txt
@@ -0,0 +1 @@
+This is file1.
diff --git a/hello.txt b/hello.txt
new file mode 100644
index 0000000..2d832d9
--- /dev/null
+++ b/hello.txt
@@ -0,0 +1 @@
+hello,world
```
