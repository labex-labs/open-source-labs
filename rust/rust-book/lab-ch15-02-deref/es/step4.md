# Definiendo Nuestro Propio Puntero Inteligente

Vamos a construir un puntero inteligente similar al tipo `Box<T>` proporcionado por la biblioteca estándar para experimentar cómo los punteros inteligentes se comportan de manera diferente a las referencias por defecto. Luego veremos cómo agregar la capacidad de usar el operador de dereferencia.

El tipo `Box<T>` se define en última instancia como una struct tupla con un elemento, por lo que la Lista 15-8 define un tipo `MyBox<T>` de la misma manera. También definiremos una función `new` para coincidir con la función `new` definida en `Box<T>`.

Nombre de archivo: `src/main.rs`

```rust
 1 struct MyBox<T>(T);

impl<T> MyBox<T> {
  2 fn new(x: T) -> MyBox<T> {
      3 MyBox(x)
    }
}
```

Lista 15-8: Definiendo un tipo `MyBox<T>`

Definimos una struct llamada `MyBox` y declaramos un parámetro genérico `T` [1] porque queremos que nuestro tipo pueda contener valores de cualquier tipo. El tipo `MyBox` es una struct tupla con un elemento de tipo `T`. La función `MyBox::new` toma un parámetro de tipo `T` [2] y devuelve una instancia de `MyBox` que contiene el valor pasado [3].

Intentemos agregar la función `main` de la Lista 15-7 a la Lista 15-8 y cambiarla para que use el tipo `MyBox<T>` que hemos definido en lugar de `Box<T>`. El código de la Lista 15-9 no se compilará porque Rust no sabe cómo desreferenciar `MyBox`.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

Lista 15-9: Intentando usar `MyBox<T>` de la misma manera que usamos referencias y `Box<T>`

Aquí está el error de compilación resultante:

```bash
error[E0614]: el tipo `MyBox<{entero}>` no se puede desreferenciar
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^
```

Nuestro tipo `MyBox<T>` no se puede desreferenciar porque no hemos implementado esa capacidad en nuestro tipo. Para habilitar la desreferencia con el operador `*`, implementamos el trato `Deref`.
