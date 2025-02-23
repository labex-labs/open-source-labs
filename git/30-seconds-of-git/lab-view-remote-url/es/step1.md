# Ver la URL remota

Como desarrollador, es posible que necesites ver la URL de un repositorio remoto por varios motivos, como solucionar problemas con tu configuración de Git o verificar que estás trabajando con el repositorio correcto. Sin embargo, si no estás familiarizado con los comandos de Git, puede ser difícil saber cómo ver la URL remota.

Para este laboratorio, usaremos el repositorio de Git llamado `https://github.com/labex-labs/git-playground`. Para ver la URL remota de este repositorio, siga estos pasos:

1. Abra su terminal o línea de comandos.
2. Navegue hasta el directorio donde ha clonado el repositorio `git-playground`:

```shell
cd git-playground
```

3. Ejecute el siguiente comando para ver la URL remota:

```shell
git config --get remote.origin.url
```

La salida debe mostrar la URL del repositorio remoto, que en este caso es `https://github.com/labex-labs/git-playground.git`.
