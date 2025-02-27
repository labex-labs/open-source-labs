# Varios bloques impl

Cada struct está permitido tener múltiples bloques `impl`. Por ejemplo, la Lista 5-15 es equivalente al código mostrado en la Lista 5-16, que tiene cada método en su propio bloque `impl`.

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Lista 5-16: Reescribiendo la Lista 5-15 usando múltiples bloques `impl`

No hay razón para separar estos métodos en múltiples bloques `impl` aquí, pero esta es una sintaxis válida. Veremos un caso en el que múltiples bloques `impl` son útiles en el Capítulo 10, donde discutiremos tipos genéricos y rasgos.
