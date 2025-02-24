# Deshabilitar la fusión en adelantamiento rápido

Por defecto, Git utiliza la fusión en adelantamiento rápido para fusionar ramas que no tienen commits divergentes. Esto significa que si tienes una rama sin nuevos commits, Git simplemente moverá el puntero de la rama en la que estás fusionando al último commit de la rama de la que estás fusionando. Si bien esto puede ser útil en algunos casos, también puede causar problemas, especialmente cuando se trabaja en proyectos más grandes con múltiples colaboradores. Por ejemplo, si dos desarrolladores están trabajando en la misma rama y ambos realizan cambios, la fusión en adelantamiento rápido puede causar conflictos que son difíciles de resolver.

## Tareas

Para deshabilitar la fusión en adelantamiento rápido, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navegue hasta el directorio y configure la identidad.
2. Cree y cambie a una rama llamada `my-branch`, cree un archivo `hello.txt` y agregue "hello,world" a él, agréguelo al área de preparación y confirme con el mensaje "Added hello.txt".
3. Deshabilite la fusión en adelantamiento rápido para todas las ramas.
4. Vuelva a la rama `master` y fusione la rama `my-branch`, guarde y salga sin cambiar el texto.

Ahora, Git siempre creará un commit de fusión, incluso si es posible hacer un adelanto:

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch'my-branch'
```
