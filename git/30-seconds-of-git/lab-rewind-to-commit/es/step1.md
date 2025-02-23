# Retroceder a un commit específico

Como desarrollador, es posible que necesites deshacer los cambios realizados en tu repositorio de código. Por ejemplo, es posible que hayas cometido un error y necesites volver a una versión anterior de tu código. En este desafío, usarás Git para retroceder a un commit específico en un repositorio.

Para completar este laboratorio, usarás el repositorio de Git `git-playground` de `https://github.com/labex-labs/git-playground.git`. Siga estos pasos para completar el desafío:

1. Clonar el repositorio en su máquina local:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navegar hasta el repositorio:

```shell
cd git-playground
```

3. Ver el historial de commits del repositorio:

```shell
git log --oneline
```

4. Asegurarse de que el mensaje de commit al que desea retroceder sea el hash del commit "Initial commit".
5. Usar el comando `git reset <commit>` para retroceder al commit especificado. Por ejemplo, desea retroceder al commit con hash `3050fc0d3`:

```shell
git reset 3050fc0d3
```

6. Ver nuevamente el historial de commits del repositorio:

```shell
git log --oneline
```

7. Si desea eliminar los cambios y revertir a la versión anterior de su código, use el comando `git reset --hard <commit>`. Por ejemplo, desea eliminar los cambios y revertir al commit con hash `c0d30f305`:

```shell
git reset --hard c0d30f305
```

Este es el resultado de ejecutar `git log --oneline`:

```shell
c0d30f305 (HEAD -> master) Initial commit
```
