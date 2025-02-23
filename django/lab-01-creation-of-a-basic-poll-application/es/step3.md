# El servidor de desarrollo

Vamos a verificar que tu proyecto de Django funcione. Cambia al directorio externo `mysite`, si aún no lo has hecho, y ejecuta los siguientes comandos:

```bash
cd ~/project/mysite
python manage.py runserver
```

Verás la siguiente salida en la línea de comandos:

```plaintext
Realizando comprobaciones del sistema...

La comprobación del sistema no identificó ningún problema (0 silenciados).

Tienes migraciones pendientes de aplicar; tu aplicación puede no funcionar correctamente hasta que se apliquen. Ejecuta 'python manage.py migrate' para aplicarlas.

- 15:50:53 Versión de Django, utilizando las configuraciones'mysite.settings' Iniciando el servidor de desarrollo en <http://127.0.0.1:8000/> Salir del servidor con CONTROL-C.
```

Ignora la advertencia sobre migraciones de base de datos no aplicadas por ahora; ocuparemos la base de datos en breve.

Has iniciado el servidor de desarrollo de Django, un servidor web ligero escrito puramente en Python. Lo hemos incluido con Django para que puedas desarrollar cosas rápidamente, sin tener que preocuparte por configurar un servidor de producción, como Apache, hasta que estés listo para la producción.

Ahora es un buen momento para señalar: **no** uses este servidor en ningún entorno que se asemeje a un entorno de producción. Está destinado solo para uso durante el desarrollo. (Estamos en el negocio de hacer marcos de web, no servidores web.)

Ahora que el servidor está en ejecución, visita <http://127.0.0.1:8000/> con tu navegador web. O, ejecuta `curl 127.0.0.1:8000` en la terminal. Verás una página "¡Felicitaciones!", con un cohete despegando. ¡Funcionó!

En la VM de LabEx, debemos agregar el dominio de LabEx a `ALLOWED_HOSTS`. Edita `mysite/settings.py` y agrega `*` al final de `ALLOWED_HOSTS`, de modo que se vea así:

```python
ALLOWED_HOSTS = ["*"]
```

Esto le dice a Django que está permitido atender solicitudes con cualquier encabezado de host.

![Servidor de desarrollo de Django en ejecución](../assets/20230907-08-56-33-3uvbOwp3.png)

## Cambiando el puerto

Por defecto, el comando `runserver` inicia el servidor de desarrollo en la dirección IP interna en el puerto 8000.

Si quieres cambiar el puerto del servidor, pásalo como argumento de línea de comandos. Por ejemplo, este comando inicia el servidor en el puerto 8080:

```bash
python manage.py runserver 8080
```

Si quieres cambiar la IP del servidor, pásala junto con el puerto. Por ejemplo, para escuchar en todas las IP públicas disponibles (lo que es útil si estás ejecutando Vagrant o quieres mostrar tu trabajo en otros computadores de la red), utiliza:

```bash
python manage.py runserver 0.0.0.0:8080
```

Ahora, cambia a la pestaña **Web 8080** en la VM de LabEx y verás la misma página "¡Felicitaciones".

![Página del servidor de desarrollo de Django](../assets/20230907-08-58-22-M3Luydxk.png)

La documentación completa del servidor de desarrollo se puede encontrar en la referencia de `runserver`.

> Recarga automática de `runserver`
> El servidor de desarrollo recarga automáticamente el código de Python según sea necesario para cada solicitud. No es necesario reiniciar el servidor para que los cambios de código surtan efecto. Sin embargo, algunas acciones como agregar archivos no desencadenan un reinicio, por lo que tendrás que reiniciar el servidor en estos casos.
