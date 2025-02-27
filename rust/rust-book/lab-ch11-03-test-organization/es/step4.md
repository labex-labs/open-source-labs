# Probando Funciones Privadas

Existe un debate dentro de la comunidad de pruebas sobre si las funciones privadas deben ser probadas directamente, y en otros lenguajes es difícil o imposible probar funciones privadas. Independientemente de la ideología de pruebas a la que adhieres, las reglas de privacidad de Rust te permiten probar funciones privadas. Considere el código de la Lista 11-12 con la función privada `internal_adder`.

Nombre de archivo: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    internal_adder(a, 2)
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }
}
```

Lista 11-12: Probando una función privada

Tenga en cuenta que la función `internal_adder` no está marcada como `pub`. Las pruebas son simplemente código de Rust, y el módulo `tests` es simplemente otro módulo. Como discutimos en "Rutas para Referirse a un Elemento en el Árbol de Módulos", los elementos en los módulos hijos pueden usar los elementos en sus módulos ancestros. En esta prueba, traemos todos los elementos del padre del módulo `test` al alcance con `use super::*`, y luego la prueba puede llamar a `internal_adder`. Si no piensas que las funciones privadas deben ser probadas, en Rust no hay nada que te obligue a hacerlo.
