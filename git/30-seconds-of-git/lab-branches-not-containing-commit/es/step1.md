# Encontrar ramas que no contienen un commit

Estás trabajando en un proyecto con múltiples ramas y necesitas encontrar todas las ramas que no contienen un commit específico. Esto puede ser útil si quieres asegurarte de que un cambio determinado se ha aplicado a todas las ramas, o si quieres saber qué ramas están desactualizadas y necesitan actualizarse.

Para este laboratorio, usaremos el repositorio de Git denominado `https://github.com/your-username/git-playground`.

1. Clona este repositorio en tu máquina local usando el siguiente comando:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Después de clonar el repositorio, usa los siguientes comandos para navegar al directorio y configurar la identidad:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Crea y cambia a una rama `new-branch` y haz algunos cambios de código en esa rama y luego confirma los cambios, el mensaje de confirmación es "Create a new-branch branch":

```shell
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Create a new-branch branch"
```

4. Verifica el hash del mensaje de confirmación "Create a new-branch branch":

```shell
git log
```

5. Encuentra todas las ramas que no contienen un hash con el mensaje de confirmación "Create a new-branch branch". Para hacer esto, podemos usar el siguiente comando:

```shell
git branch --no-contains 31c5ac20129151af1
```

Esto mostrará una lista de todas las ramas que no contienen el commit especificado. En este caso, la salida será:

```shell
master
```

Esto significa que la rama `master` no contiene el commit con el hash `31c5ac20129151af1`.
