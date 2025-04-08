# Ejecutar una sola prueba

Podemos pasar el nombre de cualquier función de prueba a `cargo test` para ejecutar solo esa prueba:

```bash

```

Solo se ejecutó la prueba con el nombre `one_hundred`; las otras dos pruebas no coincidían con ese nombre. La salida de la prueba nos informa de que teníamos más pruebas que no se ejecutaron al mostrar `2 filtradas` al final.

No podemos especificar los nombres de múltiples pruebas de esta manera; solo se usará el primer valor dado a `cargo test`. Pero hay una forma de ejecutar múltiples pruebas.
