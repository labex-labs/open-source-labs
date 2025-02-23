# Cambiar a una rama

Has estado trabajando en un proyecto en un repositorio Git llamado `https://github.com/labex-labs/git-playground`. Tu equipo ha creado una nueva rama llamada `feature-1` para trabajar en una nueva característica. Necesitas cambiar a la rama `feature-1` para continuar trabajando en la característica.

1. Clona el repositorio Git:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navega hasta el directorio del repositorio:

```shell
cd git-playground
```

3. Lista todas las ramas en el repositorio:

```shell
git branch
```

Salida:

```shell
feature-1
* master
```

4. Cambia a la rama `feature-1`:

```shell
git checkout feature-1
```

Salida:

```shell
Switched to branch 'feature-1'
```

5. Verifica que ahora estás en la rama `feature-1`:

```shell
git branch
```

Salida:

```shell
* feature-1
master
```
