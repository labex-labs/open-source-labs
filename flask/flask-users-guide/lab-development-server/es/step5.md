# La dirección ya está en uso

Si ve un `OSError` con el mensaje "La dirección ya está en uso" al intentar iniciar el servidor, significa que otro programa ya está utilizando el puerto 5000, que es el puerto predeterminado para el servidor de desarrollo. Puede identificar y detener el otro programa o elegir un puerto diferente.

Para identificar el proceso que utiliza el puerto 5000, puede usar el comando `netstat` o `lsof`. A continuación, se presentan ejemplos para Linux, macOS y Windows:

- Linux:

```bash
netstat -nlp | grep 5000
```

- macOS / Linux:

```bash
lsof -P -i :5000
```

- Windows:

```bash
-ano > netstat | findstr 5000
```

Una vez que haya identificado el proceso, puede usar otras herramientas del sistema operativo para detenerlo. Después de detener el proceso, debería poder ejecutar el servidor de desarrollo sin problemas.
