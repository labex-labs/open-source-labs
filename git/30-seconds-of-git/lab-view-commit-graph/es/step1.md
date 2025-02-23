# Ver un gráfico visual del repositorio

Como desarrollador, es posible que necesites ver la historia de un repositorio para entender cómo ha cambiado el código a lo largo del tiempo. Sin embargo, simplemente ver una lista de commits puede resultar abrumador y difícil de entender. Aquí es donde entra el gráfico de Git. Al visualizar la historia de un repositorio, puedes ver rápidamente cómo ha evolucionado el código e identificar cualquier problema o error que pueda haber sido introducido.

Para ver un gráfico visual de un repositorio de Git, puedes usar el comando `git log` con la opción `--graph`. Por ejemplo, supongamos que quieres ver la historia del repositorio `git-playground` en GitHub.

Una vez que hayas clonado el repositorio, puedes navegar hasta el directorio y usar el comando `git log` para ver el gráfico:

```shell
cd git-playground
git log --pretty=oneline --graph --decorate --all
```

Esto mostrará un gráfico visual de todos los commits y ramas del repositorio, lo que te permitirá ver cómo ha evolucionado el código a lo largo del tiempo.

Este es el resultado final:

```
* d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
* cf80005e40a3c661eb212fcea5fad06f8283f08f Added file1.txt
* b00b9374a7c549d1af111aa777fdcc868d8a2a01 Initial commit
```
