# Configurar la información de usuario de Git

Acabas de comenzar a trabajar en un nuevo proyecto y quieres configurar tu información de usuario para Git. Quieres asegurarte de que tu nombre y dirección de correo electrónico estén asociados a cualquier cambio que realices en el repositorio.

Para este laboratorio, usaremos el repositorio de Git llamado `https://github.com/labex-labs/git-playground`. Sigue estos pasos para configurar tu información de usuario para este repositorio:

1. Clona el repositorio usando el siguiente comando:

```
git clone https://github.com/labex-labs/git-playground.git
```

2. Navega al repositorio clonado usando el siguiente comando:

```
cd git-playground
```

3. Utiliza el comando `git config` para establecer tu información de usuario para el repositorio. Por ejemplo, si tu dirección de correo electrónico es `jane.doe@example.com` y tu nombre es `Jane Doe`, usarías los siguientes comandos:

```
git config user.email "jane.doe@example.com"
git config user.name "Jane Doe"
```

4. Verifica que tu información de usuario se haya configurado correctamente usando el siguiente comando: `git config --list`. Deberías ver tu dirección de correo electrónico y nombre listados bajo las claves `user.email` y `user.name`, respectivamente.

Este es el resultado después de completar el laboratorio:

![Git user configuration result](../assets/challenge-config-user-step1-1.png)
