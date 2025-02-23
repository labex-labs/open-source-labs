# Crear un commit vacío

Necesitas crear un commit vacío en tu repositorio de Git. Esto puede ser útil en varios casos, como:

- Desencadenar un proceso de compilación
- Crear un commit de marcador de posición
- Marcar un punto específico en el historial del repositorio

Para esta práctica, vamos a utilizar el repositorio de `https://github.com/labex-labs/git-playground`:

1. Clona el repositorio en tu máquina local utilizando el comando `git clone https://github.com/labex-labs/git-playground`.
2. Navega hasta el directorio del repositorio utilizando el comando `cd git-playground` y configura tu cuenta de GitHub en el entorno utilizando los comandos `git config --global user.name "tu-nombre-de-usuario"` y `git config --global user.email "tu-correo-electrónico"`.
3. Utiliza el comando `git commit --allow-empty -m "Commit vacío"` para crear un commit vacío con el mensaje "Commit vacío".
4. Verifica que se haya creado el commit vacío utilizando el comando `git log --name-status HEAD^..HEAD`.

Aquí es donde se ejecuta `git log --name-status HEAD^..HEAD` y el resultado:

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
