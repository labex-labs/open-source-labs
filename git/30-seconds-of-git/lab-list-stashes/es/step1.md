# Listar todos los almacenamientos temporales

Estás trabajando en un proyecto en un repositorio Git y has hecho algunos cambios que aún no están listos para ser confirmados. Decides guardar temporalmente estos cambios para poder trabajar en una tarea diferente. Más tarde, quieres ver una lista de todos los almacenamientos temporales que has creado para poder decidir cuál aplicar. ¿Cómo se listan todos los almacenamientos temporales en un repositorio Git?

1. Navega hasta el directorio `git-playground`:

```
cd git-playground
```

2. Crea un nuevo archivo llamado `test.txt` y agrega algún contenido a él:

```
echo "hello,world" > test.txt
git add.
```

3. Utiliza el siguiente comando para guardar temporalmente tus cambios:

```
git stash save "Added test.txt"
```

4. Crea otro nuevo archivo llamado `test2.txt` y agrega algún contenido a él:

```
echo "hello,labex" > test2.txt
git add.
```

5. Utiliza el siguiente comando para guardar temporalmente tus cambios:

```
git stash save "Added test2.txt"
```

6. Utiliza el siguiente comando para listar todos los almacenamientos temporales:

```
git stash list
```

Deberías ver una salida similar a la siguiente:

```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```
