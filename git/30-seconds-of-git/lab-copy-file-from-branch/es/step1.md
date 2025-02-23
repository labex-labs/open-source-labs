# Copiar un archivo de otra rama

Estás trabajando en un proyecto en un repositorio de Git llamado `https://github.com/labex-labs/git-playground.git`. Tienes dos ramas llamadas `feature-1` y `feature-2`. Necesitas copiar el archivo `hello.txt` de la rama `feature-1` a la rama `feature-2`.

1. Clona el repositorio:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navega al directorio y configura la identidad:

```shell
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

3. Crea y cambia a la rama `feature-1` y crea un archivo de texto llamado `hello.txt` y escribe la cadena "hello,world" en él y confirma el archivo con el mensaje "agregar hello.txt":

```shell
git checkout -b feature-1
echo "hello,world" > hello.txt
git add.
git commit -m "agregar hello.txt"
```

4. Crea y cambia a la rama `feature-2` después de cambiar a la rama `master`:

```shell
git checkout master
git checkout -b feature-2
```

5. Copia el archivo `hello.txt` de la rama `feature-1` a la rama `feature-2` y confirma con el mensaje de confirmación "copiar hello.txt":

```shell
git checkout feature-1 hello.txt
git commit -am "copiar hello.txt"
```

6. Verifica que el archivo `hello.txt` se haya copiado a la rama `feature-2`:

```shell
ll
```

Deberías ver el archivo `hello.txt` en la lista de archivos de la rama `feature-2`:

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
