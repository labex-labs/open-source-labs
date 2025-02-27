# Corrigiendo el Manejo de Errores

Ahora trabajaremos en corregir nuestro manejo de errores. Recuerda que intentar acceder a los valores en el vector `args` en el índice 1 o índice 2 hará que el programa se detenga con un error si el vector contiene menos de tres elementos. Intenta ejecutar el programa sin ningún argumento; se verá así:

```bash
$ cargo run
   Compilando minigrep v0.1.0 (file:///projects/minigrep)
    Terminada la compilación en modo desarrollo [no optimizada + información de depuración] en 0.0s
     Ejecutando `target/debug/minigrep`
hilo'main' se detuvo con un error en 'índice fuera de los límites: la longitud es 1 pero el índice es 1', src/main.rs:27:21
nota: ejecuta con la variable de entorno `RUST_BACKTRACE=1` para mostrar una traza de pila
```

La línea `índice fuera de los límites: la longitud es 1 pero el índice es 1` es un mensaje de error destinado a los programadores. No ayudará a nuestros usuarios finales a entender qué deben hacer en su lugar. Vamos a corregir eso ahora.
