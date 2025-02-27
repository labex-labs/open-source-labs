# El lifetime estático

Un lifetime especial que debemos discutir es `'static`, que denota que la referencia afectada _puede_ vivir durante toda la duración del programa. Todos los literales de cadena tienen el lifetime `'static`, que podemos anotar como sigue:

```rust
let s: &'static str = "I have a static lifetime.";
```

El texto de esta cadena se almacena directamente en el binario del programa, que siempre está disponible. Por lo tanto, el lifetime de todos los literales de cadena es `'static`.

Es posible que veas sugerencias para usar el lifetime `'static` en mensajes de error. Pero antes de especificar `'static` como el lifetime de una referencia, piensa en si la referencia que tienes realmente vive durante toda la vida útil de tu programa o no, y si quieres que lo haga. En la mayoría de los casos, un mensaje de error que sugiere el lifetime `'static` se produce al intentar crear una referencia colgante o una incompatibilidad de los lifetimes disponibles. En tales casos, la solución es corregir esos problemas, no especificar el lifetime `'static`.
