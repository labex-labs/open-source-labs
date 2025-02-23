# Automatizar la creación de ramas upstream

Como desarrollador, quieres automatizar el proceso de creación de ramas upstream al empujar para evitar el fastidio de crear manualmente la rama en el repositorio remoto.

Para este laboratorio, vas a bifurcar el repositorio `https://github.com/labex-labs/git-playground` a tu cuenta, usando el repositorio `git-playground` en tu cuenta para crear automáticamente la rama upstream al empujar.

1. En el sitio web de GitHub, inicia sesión en tu cuenta y encuentra `https://github.com/labex-labs/git-playground` para bifurcar el repositorio a tu cuenta.
2. En la página de tu propio repositorio bifurcado, haz clic en el botón `Code` y copia la URL del repositorio.
3. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

4. Usa el siguiente comando para habilitar la creación automática de ramas upstream al empujar:

```shell
git config --global push.default current
```

5. Empuja una nueva rama llamada `new-feature`, que no existe en el repositorio remoto:

```shell
git checkout -b new-feature
git push
```

6. Verifica que la nueva rama se haya creado en el repositorio remoto:

```shell
git ls-remote --heads origin
```

Este es el resultado después de completar el laboratorio:

![automatic upstream branch result](../assets/challenge-automatic-push-upstream-step1-1.png)
