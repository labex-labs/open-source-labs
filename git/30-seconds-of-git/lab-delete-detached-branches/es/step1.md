# Eliminar ramas desatadas

Tienes un repositorio Git con varias ramas desatadas que ya no necesitas. Estas ramas están desordenando tu repositorio y dificultando su gestión. Quieres eliminar todas las ramas desatadas para limpiar tu repositorio.

Para completar este laboratorio, utilizarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`. No marque "Copiar solo la rama master".

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Dado que hay una rama `feature-branch` en el repositorio remoto, cambia a `feature-branch`, lo que hará que la `feature-branch` local siga la rama `feature-branch` del repositorio remoto y elimina la rama `feature-branch` en el repositorio remoto:

```shell
git checkout feature-branch
git push origin --delete feature-branch
```

3. Ver la relación de seguimiento entre las ramas locales y las ramas remotas que siguen:

```shell
git branch -vv
```

4. Vuelve a la rama `master`:

```shell
git checkout master
```

5. Elimina todas las ramas desatadas de tu repositorio local:

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

6. Verifica que las ramas desatadas hayan sido eliminadas:

```shell
git branch
```

La salida solo debe mostrar las ramas que están asociadas a una rama específica:

```shell
* master d22f46b [origin/master] Added file2.txt
```
