# Comprobar dónde se escriben los errores

Primero, observemos cómo el contenido impreso por `minigrep` se está escribiendo actualmente en la salida estándar, incluyendo cualquier mensaje de error que queramos escribir en el error estándar en lugar de eso. Lo haremos redirigiendo el flujo de salida estándar a un archivo mientras causamos intencionalmente un error. No redirigiremos el flujo de error estándar, por lo que cualquier contenido enviado al error estándar seguirá mostrándose en la pantalla.

Se espera que los programas de línea de comandos envíen mensajes de error al flujo de error estándar para que aún podamos ver los mensajes de error en la pantalla incluso si redirigimos el flujo de salida estándar a un archivo. Nuestro programa no se comporta bien en este momento: ¡vamos a ver que guarda la salida del mensaje de error en un archivo en lugar de mostrarlo en la pantalla!

Para demostrar este comportamiento, ejecutaremos el programa con `>` y la ruta del archivo, _output.txt_, al que queremos redirigir el flujo de salida estándar. No pasaremos ningún argumento, lo que debería causar un error:

```bash
cargo run > output.txt
```

La sintaxis `>` le dice a la shell que escriba el contenido de la salida estándar en _output.txt_ en lugar de en la pantalla. No vimos el mensaje de error que esperábamos impreso en la pantalla, por lo que eso significa que debe haber terminado en el archivo. Esto es lo que contiene _output.txt_:

```rust
Problem parsing arguments: not enough arguments
```

Sí, nuestro mensaje de error se está imprimiendo en la salida estándar. Es mucho más útil que los mensajes de error como este se impriman en el error estándar para que solo los datos de una ejecución exitosa terminen en el archivo. Vamos a cambiar eso.
