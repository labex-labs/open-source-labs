# Mutabilidad Interior: Un Préstamo Mutable a un Valor Inmutable

Una consecuencia de las reglas de préstamo es que cuando tienes un valor inmutable, no puedes préstamo mutarlo. Por ejemplo, este código no se compilará:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = &mut x;
}
```

Si intentaras compilar este código, obtendrías el siguiente error:

```bash
error[E0596]: no se puede prestar `x` como mutable, ya que no está
declarado como mutable
 --> src/main.rs:3:13
  |
2 |     let x = 5;
  |         - ayuda: considere cambiar esto a ser mutable: `mut x`
3 |     let y = &mut x;
  |             ^^^^^^ no se puede prestar como mutable
```

Sin embargo, hay situaciones en las que sería útil que un valor se mutara a sí mismo en sus métodos pero apareciera inmutable para el resto del código. El código fuera de los métodos del valor no sería capaz de mutar el valor. Usar `RefCell<T>` es una manera de obtener la capacidad de tener mutabilidad interior, pero `RefCell<T>` no evita completamente las reglas de préstamo: el verificador de préstamos del compilador permite esta mutabilidad interior, y las reglas de préstamo se comprueban en tiempo de ejecución en lugar de eso. Si violas las reglas, obtendrás un `panic!` en lugar de un error del compilador.

Veamos un ejemplo práctico en el que podemos usar `RefCell<T>` para mutar un valor inmutable y veamos por qué eso es útil.
