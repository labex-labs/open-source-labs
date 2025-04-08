# Git Cherry-Pick

Como desarrollador, estás trabajando en un proyecto con múltiples ramas. Has identificado un cambio específico que se hizo en un commit anterior que deseas aplicar a tu rama actual. Sin embargo, no quieres fusionar la rama completa porque contiene otros cambios que no necesitas. En este escenario, puedes usar el comando `git cherry-pick` para aplicar el cambio específico a tu rama actual.

Para este laboratorio, usemos el repositorio de `https://github.com/labex-labs/git-playground`. Sigue los pasos a continuación para completar el reto:

1. Clona el repositorio, navega al directorio y configura la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Crea y cambia a una rama llamada `one-branch`, crea un archivo llamado `hello.txt`, escribe "hello,world" en él, agrégalo al área de preparación (staging area) y haz un commit con el mensaje "add hello.txt":

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

3. Identifica el hash del commit creado en el paso anterior para aplicarlo a la rama `master`:

```shell
git log
```

4. Cambia a la rama `master` y aplica el cambio a la rama `master`:

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. Verifica que el cambio se haya aplicado a la rama `master`:

```shell
git log
```

Este es el resultado de ejecutar `git log` en la rama `master`:

```shell

ADD hello.txt
```
