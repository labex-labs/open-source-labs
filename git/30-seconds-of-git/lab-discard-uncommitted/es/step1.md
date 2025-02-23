# Descarta los cambios no confirmados

Has realizado algunos cambios en tu repositorio local de Git, pero aún no los has confirmado. Sin embargo, has decidido que ya no quieres mantener estos cambios y los quieres descartar. El problema es encontrar una forma de descartar todos los cambios no confirmados en la rama actual.

Para completar este desafío, utilizarás el repositorio de Git denominado `https://github.com/labex-labs/git-playground` en el directorio. Sigue los pasos siguientes:

1. Clona el repositorio en tu máquina local utilizando el comando `git clone https://github.com/labex-labs/git-playground.git`.
2. Navega hasta el repositorio clonado utilizando el comando `cd git-playground`.
3. Haz algunos cambios en los archivos del repositorio, pero no los confirmes utilizando los comandos `echo "hello,world" > hello.txt` y `git add.`.
4. Utiliza el comando `git status` para ver los cambios que has realizado.
5. Descarta todos los cambios no confirmados utilizando el comando `git reset --hard HEAD`.
6. Utiliza el comando `git status` nuevamente para confirmar que todos los cambios han sido descartados.

Este es el resultado de ejecutar `git status`:

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
