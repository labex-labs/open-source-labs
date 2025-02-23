# Cambiar el autor del último commit

Acabas de hacer un commit en tu repositorio de Git, pero te has dado cuenta de que el nombre y la dirección de correo electrónico del autor son incorrectos. Quieres actualizar la información del autor sin cambiar el contenido del commit. ¿Cómo puedes lograr esto con Git?

## Tareas

Para cambiar el autor del último commit, puedes usar un comando. Este comando te permite modificar el último commit en tu repositorio de Git.

1. Navega hasta el repositorio y configura la información de identidad de Git usando tu cuenta de GitHub.
2. Cambia el autor del último commit a `Duck Quackers`, cuya dirección de correo electrónico es `cool.duck@qua.ck` y guarda el contenido.
3. Verifica que la información del autor se haya actualizado.

Deberías ver que el autor del último commit ahora es `Duck Quackers`:

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
