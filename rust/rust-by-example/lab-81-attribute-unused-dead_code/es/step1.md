# `dead_code`

El compilador proporciona un _lint_ `dead_code` que advertirá sobre funciones no utilizadas. Se puede utilizar un _atributo_ para deshabilitar el lint.

```rust
fn used_function() {}

// `#[allow(dead_code)]` es un atributo que deshabilita el lint `dead_code`
#[allow(dead_code)]
fn unused_function() {}

fn noisy_unused_function() {}
// FIXME ^ Agrega un atributo para suprimir la advertencia

fn main() {
    used_function();
}
```

Ten en cuenta que en programas reales, debes eliminar el código muerto (dead code). En estos ejemplos, permitiremos el código muerto en algunos lugares debido a la naturaleza interactiva de los ejemplos.
