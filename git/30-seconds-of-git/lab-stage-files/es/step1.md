# Agregar archivos al área de preparación

Has estado trabajando en un proyecto almacenado en un repositorio de Git llamado `https://github.com/labex-labs/git-playground`. Has realizado algunos cambios en el repositorio de código y quieres confirmar estos cambios en el repositorio. Sin embargo, solo quieres confirmar cambios específicos y no todos los cambios que has realizado. Para hacer esto, necesitas agregar los archivos al área de preparación.

1. Realizarás algunos cambios en el directorio `git-playground`:

```shell
echo "hello" > index.html
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```

2. Agregar estos archivos al área de preparación:

```shell
git add index.html style.css
```

3. Ver el estado del directorio de trabajo actual y del área de preparación, incluyendo información sobre qué archivos se han modificado, qué archivos se han agregado al área de preparación, etc:

```shell
git status
```

4. Alternativamente, agregar todos los archivos con una extensión `.js`:

```shell
git add *.js
```

5. Ver nuevamente el estado del directorio de trabajo actual y del área de preparación:

```shell
git status
```

6. También puedes agregar todos los cambios al área de preparación:

```shell
git add.
```

7. Ver nuevamente el estado del directorio de trabajo actual y del área de preparación:

```shell
git status
```

Este es el resultado final:

![Git staging area status](../assets/challenge-stage-files-step1-1.png)
