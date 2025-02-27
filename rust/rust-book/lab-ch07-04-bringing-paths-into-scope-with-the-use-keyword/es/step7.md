# El operador glob

Si queremos traer a todos los elementos públicos definidos en una ruta al alcance, podemos especificar esa ruta seguida del operador glob `*`:

```rust
use std::collections::*;
```

Esta declaración `use` trae todos los elementos públicos definidos en `std::collections` al alcance actual. Tenga cuidado al usar el operador glob. El glob puede hacer que sea más difícil saber qué nombres están en el alcance y dónde se definió un nombre usado en su programa.

El operador glob se usa a menudo en pruebas para traer todo lo que se va a probar al módulo `tests`; hablaremos de eso en "Cómo escribir pruebas". El operador glob también se usa a veces como parte del patrón preludio: consulte la documentación de la biblioteca estándar para obtener más información sobre ese patrón.
