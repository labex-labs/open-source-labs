# Filtrado para ejecutar múltiples pruebas

Podemos especificar una parte del nombre de una prueba, y cualquier prueba cuyo nombre coincida con ese valor se ejecutará. Por ejemplo, dado que dos de los nombres de nuestras pruebas contienen `add`, podemos ejecutarlas dos ejecutando `cargo test add`:

```bash

```

Este comando ejecutó todas las pruebas con `add` en el nombre y filtró la prueba llamada `one_hundred`. También tenga en cuenta que el módulo en el que aparece una prueba se convierte en parte del nombre de la prueba, por lo que podemos ejecutar todas las pruebas en un módulo filtrando por el nombre del módulo.
