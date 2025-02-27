# En definiciones de métodos

Podemos implementar métodos en structs y enums (como lo hicimos en el Capítulo 5) y también usar tipos genéricos en sus definiciones. La Lista 10-9 muestra el struct `Point<T>` que definimos en la Lista 10-6 con un método llamado `x` implementado en él.

Nombre de archivo: `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}
```

Lista 10-9: Implementando un método llamado `x` en el struct `Point<T>` que devolverá una referencia al campo `x` del tipo `T`

Aquí, hemos definido un método llamado `x` en `Point<T>` que devuelve una referencia a los datos en el campo `x`.

Tenga en cuenta que tenemos que declarar `T` justo después de `impl` para poder usar `T` para especificar que estamos implementando métodos en el tipo `Point<T>`. Al declarar `T` como un tipo genérico después de `impl`, Rust puede identificar que el tipo en los corchetes angulares en `Point` es un tipo genérico en lugar de un tipo concrete. Podríamos haber elegido un nombre diferente para este parámetro genérico que el parámetro genérico declarado en la definición del struct, pero usar el mismo nombre es convencional. Los métodos escritos dentro de un `impl` que declara el tipo genérico se definirán en cualquier instancia del tipo, sin importar qué tipo concrete termine sustituyendo al tipo genérico.

También podemos especificar restricciones en los tipos genéricos al definir métodos en el tipo. Podríamos, por ejemplo, implementar métodos solo en instancias de `Point<f32>` en lugar de en instancias de `Point<T>` con cualquier tipo genérico. En la Lista 10-10 usamos el tipo concrete `f32`, lo que significa que no declaramos ningún tipo después de `impl`.

Nombre de archivo: `src/main.rs`

```rust
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

Lista 10-10: Un bloque `impl` que solo se aplica a un struct con un tipo concrete particular para el parámetro de tipo genérico `T`

Este código significa que el tipo `Point<f32>` tendrá un método `distance_from_origin`; otras instancias de `Point<T>` donde `T` no es del tipo `f32` no tendrán este método definido. El método mide qué tan lejos está nuestro punto del punto en las coordenadas (0.0, 0.0) y utiliza operaciones matemáticas que solo están disponibles para tipos de punto flotante.

Los parámetros de tipo genérico en una definición de struct no siempre son los mismos que los que se usan en las firmas de métodos de ese mismo struct. La Lista 10-11 usa los tipos genéricos `X1` y `Y1` para el struct `Point` y `X2` `Y2` para la firma del método `mixup` para que el ejemplo sea más claro. El método crea una nueva instancia de `Point` con el valor de `x` del `Point` `self` (del tipo `X1`) y el valor de `y` del `Point` pasado como argumento (del tipo `Y2`).

Nombre de archivo: `src/main.rs`

```rust
struct Point<X1, Y1> {
    x: X1,
    y: Y1,
}

1 impl<X1, Y1> Point<X1, Y1> {
  2 fn mixup<X2, Y2>(
        self,
        other: Point<X2, Y2>,
    ) -> Point<X1, Y2> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}

fn main() {
  3 let p1 = Point { x: 5, y: 10.4 };
  4 let p2 = Point { x: "Hello", y: 'c' };

  5 let p3 = p1.mixup(p2);

  6 println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
```

Lista 10-11: Un método que usa tipos genéricos diferentes de su definición de struct

En `main`, hemos definido un `Point` que tiene un `i32` para `x` (con el valor `5`) y un `f64` para `y` (con el valor `10.4` \[3\]). La variable `p2` es un struct `Point` que tiene una porción de cadena para `x` (con el valor `"Hello"`) y un `char` para `y` (con el valor `c` \[4\]). Llamar a `mixup` en `p1` con el argumento `p2` nos da `p3` \[5\], que tendrá un `i32` para `x` porque `x` vino de `p1`. La variable `p3` tendrá un `char` para `y` porque `y` vino de `p2`. La llamada a la macro `println!` \[6\] imprimirá `p3.x = 5, p3.y = c`.

El propósito de este ejemplo es demostrar una situación en la que algunos parámetros genéricos se declaran con `impl` y algunos se declaran con la definición del método. Aquí, los parámetros genéricos `X1` y `Y1` se declaran después de `impl` \[1\] porque van con la definición del struct. Los parámetros genéricos `X2` y `Y2` se declaran después de `fn mixup` \[2\] porque solo son relevantes para el método.
