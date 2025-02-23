# Deshabilitar la fusión en adelantamiento rápido

Por defecto, Git utiliza la fusión en adelantamiento rápido para fusionar ramas que no tienen commits divergentes. Esto significa que si tienes una rama sin nuevos commits, Git simplemente moverá el puntero de la rama en la que estás fusionando al último commit de la rama de la que estás fusionando. Si bien esto puede ser útil en algunos casos, también puede causar problemas, especialmente cuando se trabaja en proyectos más grandes con múltiples colaboradores. Por ejemplo, si dos desarrolladores están trabajando en la misma rama y ambos realizan cambios, la fusión en adelantamiento rápido puede causar conflictos que son difíciles de resolver.

Para deshabilitar la fusión en adelantamiento rápido, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

2. Crea y cambia a una rama llamada `my-branch`, crea un archivo `hello.txt` y agrega "hello,world" a él, agréguelo al área de preparación y confírmalo con el mensaje "Agregado hello.txt":

```shell
git checkout -b my-branch
echo "hello,world" > hello.txt
git add.
git commit -m "Agregado hello.txt"
```

3. Ejecuta el siguiente comando para deshabilitar la fusión en adelantamiento rápido:

```shell
git config --add merge.ff false
```

Esto deshabilitará la fusión en adelantamiento rápido para todas las ramas, incluso si es posible. Puedes usar la bandera `--global` para configurar esta opción globalmente:

```shell
git config --global --add merge.ff false
```

4. Vuelve a la rama `master` y fusiona la rama `my-branch`, guarda y sale sin cambiar el texto:

```shell
git checkout master
git merge my-branch
```

Ahora, Git siempre creará un commit de fusión, incluso si es posible hacer un adelanto rápido:

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch'my-branch'
```
