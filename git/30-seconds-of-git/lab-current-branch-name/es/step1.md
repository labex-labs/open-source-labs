# Obtener el nombre de la rama actual

Escribe un comando que imprima el nombre de la rama actual en un repositorio de Git.

Supongamos que estás trabajando en un proyecto almacenado en el repositorio `https://github.com/labex-labs/git-playground`. Has realizado algunos cambios en el archivo `README.md` y quieres registrar los cambios en la rama actual. Sin embargo, antes de hacerlo, quieres asegurarte de que estés en la rama correcta.

Para comprobar la rama actual, puedes utilizar el siguiente comando:

```shell
git rev-parse --abbrev-ref HEAD
```

Esto imprimirá el nombre de la rama actual en la consola. Por ejemplo, si estás actualmente en la rama `master`, la salida será:

```shell
master
```

Si cambias a una rama diferente, como `feature-branch`, la salida cambiará en consecuencia:

```shell
git checkout -b feature-branch
git rev-parse --abbrev-ref HEAD
```

Esto producirá la siguiente salida:

```shell
feature-branch
```
