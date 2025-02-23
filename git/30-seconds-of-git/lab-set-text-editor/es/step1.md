# Configurar el editor de texto de git

Para este laboratorio, vamos a utilizar el repositorio de `https://github.com/labex-labs/git-playground`. Quieres configurar el editor de texto utilizado por Git al editor que prefieres.

1. Clona el repositorio `git-playground`:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Navega al repositorio clonado y configura la identidad:

```shell
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

3. Configura Git para que use tu editor de texto preferido (en este ejemplo, usaremos vim):

```shell
git config --global core.editor "vim"
```

4. Haz un cambio en un archivo y prepáralo para el commit:

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. Confirma el cambio:

```shell
git commit
```

6. Tu editor de texto preferido (en este ejemplo, vim) debería abrirse con el mensaje de commit. Escribe tu mensaje de commit "Actualizar hello.txt" y guarda el archivo.
7. Cierra el editor de texto. El commit se realizará con el mensaje que escribiste.

Este es el resultado final:

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Actualizar hello.txt
```
