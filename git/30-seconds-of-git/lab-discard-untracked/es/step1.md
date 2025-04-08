# Descarta los cambios no rastreados

Estás trabajando en un proyecto utilizando Git y has realizado algunos cambios en tu directorio de trabajo. Sin embargo, te das cuenta de que no necesitas estos cambios y los quieres descartar. Quieres descartar todos los cambios no rastreados en la rama actual.

Para completar este laboratorio, utilizarás el repositorio de Git denominado `https://github.com/labex-labs/git-playground`. Sigue estos pasos:

1. Navega hasta el directorio del repositorio:

```shell
cd git-playground
```

2. Verifica el estado de tu directorio de trabajo:

```shell
git status
```

Deberías ver la siguiente salida:

```shell

```

3. Descarta todos los cambios no rastreados en la rama actual:

```shell
git clean -f -d
```

4. Verifica nuevamente el estado de tu directorio de trabajo:

```shell
git status
```

Deberías ver la siguiente salida:

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

El comando `git clean -f -d` ha descartado todos los cambios no rastreados en la rama actual.
