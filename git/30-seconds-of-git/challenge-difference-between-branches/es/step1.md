# Diferencia entre ramas

Has estado trabajando en un proyecto con tu equipo y has creado una rama llamada `feature-1` para trabajar en una nueva característica. Tu compañero de equipo también ha creado una rama llamada `feature-2` para trabajar en una característica diferente. Quieres comparar los cambios entre las dos ramas para ver qué se ha agregado, modificado o eliminado. ¿Cómo puedes ver la diferencia entre las dos ramas?

## Tareas

Supongamos que tu cuenta de GitHub clona un repositorio llamado `git-playground` de `https://github.com/labex-labs/git-playground.git`.

1. Navega hasta el directorio del repositorio y configura tu identidad de GitHub.
2. Cambia a la rama `feature-1` y agrega "hello" al archivo `README.md`, agréguelo al área de preparación y confirma, el mensaje de confirmación es "Agregar nuevo contenido a README.md".
3. Cambia a la rama `feature-2` y agrega "world" al archivo `index.html`, agréguelo al área de preparación y confirma, el mensaje de confirmación es "Actualizar archivo index.html".
4. Ver la diferencia entre las dos ramas.

La salida debe mostrar la diferencia entre las ramas `feature-1` y `feature-2`. Esto muestra cómo se verá el resultado final:

```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
# git-playground
Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
