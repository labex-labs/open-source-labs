# Usando `Box<T>` Como una Referencia

Podemos reescribir el código de la Lista 15-6 para usar un `Box<T>` en lugar de una referencia; el operador de dereferencia usado en el `Box<T>` de la Lista 15-7 funciona de la misma manera que el operador de dereferencia usado en la referencia de la Lista 15-6.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let x = 5;
  1 let y = Box::new(x);

    assert_eq!(5, x);
  2 assert_eq!(5, *y);
}
```

Lista 15-7: Usando el operador de dereferencia en un `Box<i32>`

La principal diferencia entre la Lista 15-7 y la Lista 15-6 es que aquí establecemos `y` como una instancia de un box que apunta a una copia del valor de `x` en lugar de una referencia que apunta al valor de `x` [1]. En la última afirmación [2], podemos usar el operador de dereferencia para seguir el puntero del box de la misma manera que lo hicimos cuando `y` era una referencia. A continuación, exploraremos lo que es especial de `Box<T>` que nos permite usar el operador de dereferencia definiendo nuestro propio tipo de box.
