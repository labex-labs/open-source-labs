# Usando Supertraits

A veces, es posible que escribas una definición de trait que depende de otro trait: para que un tipo implemente el primer trait, quieres exigir que ese tipo también implemente el segundo trait. Lo harías para que la definición de tu trait pueda aprovechar los elementos asociados del segundo trait. El trait en el que se basa la definición de tu trait se llama _supertrait_ de tu trait.

Por ejemplo, digamos que queremos crear un trait `OutlinePrint` con un método `outline_print` que imprimirá un valor dado con un formato que lo rodee de asteriscos. Es decir, dado una struct `Point` que implementa el trait `Display` de la biblioteca estándar para obtener `(x, y)`, cuando llamamos a `outline_print` en una instancia de `Point` que tiene `1` para `x` y `3` para `y`, debería imprimir lo siguiente:

    **********
    *        *
    * (1, 3) *
    *        *
    **********

En la implementación del método `outline_print`, queremos usar la funcionalidad del trait `Display`. Por lo tanto, necesitamos especificar que el trait `OutlinePrint` solo funcionará para tipos que también implementen `Display` y proporcionen la funcionalidad que `OutlinePrint` necesita. Lo podemos hacer en la definición del trait especificando `OutlinePrint: Display`. Esta técnica es similar a agregar un límite de trait al trait. La Lista 19-22 muestra una implementación del trait `OutlinePrint`.

Nombre de archivo: `src/main.rs`

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

Lista 19-22: Implementando el trait `OutlinePrint` que requiere la funcionalidad de `Display`

Debido a que hemos especificado que `OutlinePrint` requiere el trait `Display`, podemos usar la función `to_string` que se implementa automáticamente para cualquier tipo que implemente `Display`. Si intentáramos usar `to_string` sin agregar dos puntos y especificar el trait `Display` después del nombre del trait, obtendríamos un error que dice que no se encontró ningún método llamado `to_string` para el tipo `&Self` en el ámbito actual.

Veamos qué pasa cuando intentamos implementar `OutlinePrint` en un tipo que no implementa `Display`, como la struct `Point`:

Nombre de archivo: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

Obtenemos un error que dice que se requiere `Display` pero no está implementado:

```bash
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
   |
20 | impl OutlinePrint for Point {}
   |      ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
   |
3  | trait OutlinePrint: fmt::Display {
   |                     ^^^^^^^^^^^^ required by this bound in `OutlinePrint`
```

Para solucionar esto, implementamos `Display` en `Point` y cumplimos con la restricción que `OutlinePrint` requiere, así:

Nombre de archivo: `src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

Luego, implementar el trait `OutlinePrint` en `Point` se compilará correctamente, y podemos llamar a `outline_print` en una instancia de `Point` para mostrarla dentro de un contorno de asteriscos.
