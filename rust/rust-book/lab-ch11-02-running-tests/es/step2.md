# Ejecutar pruebas en paralelo o secuencialmente

Cuando ejecutas múltiples pruebas, por defecto se ejecutan en paralelo utilizando hilos, lo que significa que terminan de ejecutarse más rápido y obtienes retroalimentación más rápidamente. Debido a que las pruebas se ejecutan al mismo tiempo, debes asegurarte de que tus pruebas no dependan una de otra ni de ningún estado compartido, incluyendo un entorno compartido, como el directorio de trabajo actual o las variables de entorno.

Por ejemplo, supongamos que cada una de tus pruebas ejecuta un código que crea un archivo en el disco llamado _test-output.txt_ y escribe algunos datos en ese archivo. Luego, cada prueba lee los datos en ese archivo y afirma que el archivo contiene un valor particular, que es diferente en cada prueba. Debido a que las pruebas se ejecutan al mismo tiempo, una prueba podría sobrescribir el archivo en el intervalo de tiempo entre que otra prueba escribe y lee el archivo. La segunda prueba entonces fallará, no porque el código sea incorrecto sino porque las pruebas se han interferido entre sí mientras se ejecutan en paralelo. Una solución es asegurarse de que cada prueba escriba en un archivo diferente; otra solución es ejecutar las pruebas una a la vez.

Si no quieres ejecutar las pruebas en paralelo o si quieres un control más detallado sobre el número de hilos utilizados, puedes enviar la bandera `--test-threads` y el número de hilos que quieres utilizar al binario de prueba. Echa un vistazo al siguiente ejemplo:

```bash
cargo test -- --test-threads=1
```

Establecemos el número de hilos de prueba en `1`, lo que le dice al programa que no use ningún paralelismo. Ejecutar las pruebas con un solo hilo tardará más tiempo que ejecutarlas en paralelo, pero las pruebas no se interferirán entre sí si comparten estado.
