# Retroceder en los commits

Como desarrollador, has estado trabajando en un proyecto y has hecho varios commits. Sin embargo, te das cuenta de que los últimos commits contienen errores y necesitas volver a una versión anterior de tu código. Necesitas usar Git para retroceder en tus commits y volver a la versión anterior de tu código.

Para completar este laboratorio, usarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`. Sigue estos pasos:

1. Clona el repositorio en tu máquina local:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Crea una nueva rama llamada `rewind-commits`:

```shell
git checkout -b rewind-commits
```

3. Ver el historial de commits del repositorio y da cuenta de que el último commit contiene errores y necesitas volver a la versión anterior de tu código:

```shell
git log
```

4. Usa Git para retroceder en tus commits en 1:

```shell
git reset HEAD~1 --hard
```

5. Verifica que hayas retrocedido correctamente en tus commits:

```shell
git log
```

6. Sube tus cambios a la rama `rewind-commits`:

```shell
git push --force origin rewind-commits
```

Este es el resultado final:

```shell
cf80005 (HEAD -> rewind-commits, origin/rewind-commits) Added file1.txt
b00b937 Initial commit
```
