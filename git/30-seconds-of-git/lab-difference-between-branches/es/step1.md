# Diferencia entre ramas

Has estado trabajando en un proyecto con tu equipo y has creado una rama llamada `feature-1` para trabajar en una nueva característica. Tu compañero de equipo también ha creado una rama llamada `feature-2` para trabajar en una característica diferente. Quieres comparar los cambios entre las dos ramas para ver qué se ha agregado, modificado o eliminado. ¿Cómo puedes visualizar la diferencia entre las dos ramas?

Supongamos que tu cuenta de GitHub clona un repositorio llamado `git-playground` de `https://github.com/labex-labs/git-playground.git`. Sigue los pasos siguientes:

1. Cambia al directorio del repositorio usando el comando `cd git-playground`.
2. Configura tu cuenta de GitHub en este entorno usando los comandos `git config --global user.name "Tu Nombre"` y `git config --global user.email "tu@email.com"`.
3. Crea y cambia a la rama `feature-1` usando el comando `git checkout -b feature-1`, agrega "hello" al archivo `README.md`, agrégalo al área de preparación y confirma, el mensaje de confirmación es "Agregar nuevo contenido a README.md" usando los comandos `echo "hello" >> README.md `, `git add.` y `git commit -am "Agregar nuevo contenido a README.md"`.
4. Vuelve a la rama `master`.
5. Crea y cambia a la rama `feature-2` usando el comando `git checkout -b feature-2`, agrega "world" al archivo `index.html`, agrégalo al área de preparación y confirma, el mensaje de confirmación es "Actualizar el archivo index.html" usando los comandos `echo "world" > index.htm`, `git add.` y `git commit -am "Actualizar el archivo index.html"`.
6. Visualiza la diferencia entre las dos ramas usando el comando `git diff feature-1..feature-2`.

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
