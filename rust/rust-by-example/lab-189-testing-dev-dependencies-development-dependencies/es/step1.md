# Dependencias de desarrollo

A veces es necesario tener dependencias solo para las pruebas (o ejemplos, o benchmarks). Tales dependencias se agregan a `Cargo.toml` en la sección `[dev-dependencias]`. Estas dependencias no se propagan a otros paquetes que dependen de este paquete.

Un ejemplo de esto es [`pretty_assertions`](https://docs.rs/pretty_assertions/1.0.0/pretty_assertions/index.html), que extiende las macros estándar `assert_eq!` y `assert_ne!`, para proporcionar diferencias en color.
Archivo `Cargo.toml`:

```toml
# se omite la información estándar del crat
[dev-dependencias]
pretty_assertions = "1"
```

Archivo `src/lib.rs`:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // crat solo para uso en pruebas. No se puede usar en código no de prueba.

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
```
