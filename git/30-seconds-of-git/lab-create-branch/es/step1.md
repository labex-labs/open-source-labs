# Crea una nueva rama

Para este laboratorio, haz un fork del repositorio Git denominado `https://github.com/labex-labs/git-playground` en tu cuenta de GitHub. Estás trabajando en un proyecto en un repositorio Git denominado `https://github.com/your-username/git-playground`. Necesitas crear una nueva rama denominada `feature-1` para trabajar en una nueva característica.

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Verifica la rama actual:

```shell
git branch
```

3. Crea una nueva rama denominada `feature-1`:

```shell
git checkout -b feature-1
```

4. Verifica que ahora estás en la rama `feature-1`:

```shell
git branch
```

5. Sube los cambios al repositorio remoto:

```shell
git push -u origin feature-1
```

Esto es lo que sucede cuando ejecutas el comando `git branch -r`:

![git branch remote output](../assets/challenge-create-branch-step1-1.png)
