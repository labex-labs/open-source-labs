# Cambiar el autor del último commit

Acabas de hacer un commit en tu repositorio de Git, pero te has dado cuenta de que el nombre y la dirección de correo electrónico del autor son incorrectos. Quieres actualizar la información del autor sin cambiar el contenido del commit. ¿Cómo puedes lograr esto con Git?

Para cambiar el autor del último commit, puedes usar el comando `git commit --amend`. Este comando te permite modificar el último commit en tu repositorio de Git. Aquí te presento un ejemplo de cómo puedes cambiar el nombre y la dirección de correo electrónico del autor:

1. Clona el repositorio de Git denominado `https://github.com/labex-labs/git-playground` en tu máquina local:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Configura la información de identidad de Git usando tu cuenta de GitHub:

```shell
cd git-playground
git config user.email "tu correo"
git config user.name "tu nombre de usuario"
```

3. Utiliza el comando `git commit --amend` para modificar el autor del último commit y guardar el contenido:

```shell
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
```

4. Verifica que la información del autor se haya actualizado:

```shell
git log
```

Deberías ver que el autor del último commit ahora es `Duck Quackers`:

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
