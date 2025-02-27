# En definiciones de structs

También podemos definir structs para usar un parámetro de tipo genérico en uno o más campos usando la sintaxis `<>`. La Lista 10-6 define un struct `Point<T>` para almacenar valores de coordenadas `x` e `y` de cualquier tipo.

Nombre de archivo: `src/main.rs`

```rust
1 struct Point<T> {
  2 x: T,
  3 y: T,
}

fn main() {
    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };
}
```

Lista 10-6: Un struct `Point<T>` que almacena valores de `x` e `y` del tipo `T`

La sintaxis para usar genéricos en definiciones de structs es similar a la usada en definiciones de funciones. Primero declaramos el nombre del parámetro de tipo dentro de corchetes angulares justo después del nombre del struct \[1\]. Luego usamos el tipo genérico en la definición del struct donde de lo contrario especificaríamos tipos de datos concretos \[23\].

Tenga en cuenta que como solo hemos usado un tipo genérico para definir `Point<T>`, esta definición dice que el struct `Point<T>` es genérico sobre algún tipo `T`, y los campos `x` e `y` son _ambos_ ese mismo tipo, sea cual sea ese tipo. Si creamos una instancia de un `Point<T>` que tiene valores de diferentes tipos, como en la Lista 10-7, nuestro código no se compilará.

Nombre de archivo: `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

fn main() {
    let wont_work = Point { x: 5, y: 4.0 };
}
```

Lista 10-7: Los campos `x` e `y` deben ser del mismo tipo porque ambos tienen el mismo tipo de datos genérico `T`.

En este ejemplo, cuando asignamos el valor entero `5` a `x`, le decimos al compilador que el tipo genérico `T` será un entero para esta instancia de `Point<T>`. Luego, cuando especificamos `4.0` para `y`, que hemos definido para tener el mismo tipo que `x`, obtendremos un error de tipo no coincidente como este:

```bash
error[E0308]: mismatched types
 --> src/main.rs:7:38
  |
7 |     let wont_work = Point { x: 5, y: 4.0 };
  |                                      ^^^ expected integer, found floating-
point number
```

Para definir un struct `Point` donde `x` e `y` son ambos genéricos pero pueden tener diferentes tipos, podemos usar múltiples parámetros de tipo genérico. Por ejemplo, en la Lista 10-8, cambiamos la definición de `Point` para que sea genérica sobre los tipos `T` y `U` donde `x` es del tipo `T` y `y` es del tipo `U`.

Nombre de archivo: `src/main.rs`

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

fn main() {
    let both_integer = Point { x: 5, y: 10 };
    let both_float = Point { x: 1.0, y: 4.0 };
    let integer_and_float = Point { x: 5, y: 4.0 };
}
```

Lista 10-8: Un `Point<T, U>` genérico sobre dos tipos para que `x` e `y` puedan ser valores de diferentes tipos

Ahora todas las instancias de `Point` mostradas están permitidas. Puede usar tantos parámetros de tipo genérico en una definición como desee, pero usar más de unos cuantos hace que su código sea difícil de leer. Si encuentra que necesita muchos tipos genéricos en su código, podría indicar que su código necesita ser reorganizado en piezas más pequeñas.
