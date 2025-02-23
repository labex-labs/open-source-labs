# Ver el último commit

Estás trabajando en un proyecto con un equipo de desarrolladores y necesitas ver el último commit realizado en el repositorio Git del proyecto. Quieres ver los detalles del commit, incluyendo el mensaje del commit, el autor y la fecha.

Para ver el último commit realizado en un repositorio Git, sigue estos pasos:

1. Abre la terminal de tu computadora.
2. Navega hasta el directorio donde se encuentra el repositorio Git:

```shell
cd git-playground
```

3. Ver el último commit:

```shell
git log -1
```

La salida te mostrará los detalles del último commit, incluyendo el mensaje del commit, el autor y la fecha:

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
