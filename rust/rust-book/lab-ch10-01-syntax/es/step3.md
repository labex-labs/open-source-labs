# En definiciones de funciones

Al definir una función que utiliza genéricos, colocamos los genéricos en la firma de la función donde normalmente especificaríamos los tipos de datos de los parámetros y el valor de retorno. Hacer esto hace que nuestro código sea más flexible y proporciona más funcionalidad a los llamantes de nuestra función mientras evita la duplicación de código.

Continuando con nuestra función `largest`, la Lista 10-4 muestra dos funciones que ambas encuentran el valor más grande en un slice. Luego combinaremos estas en una sola función que utiliza genéricos.

Nombre de archivo: `src/main.rs`

```rust
fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {result}");
}
```

Lista 10-4: Dos funciones que difieren solo en sus nombres y en los tipos en sus firmas

La función `largest_i32` es la que extrajimos en la Lista 10-3 que encuentra el `i32` más grande en un slice. La función `largest_char` encuentra el `char` más grande en un slice. Los cuerpos de las funciones tienen el mismo código, así que eliminemos la duplicación introduciendo un parámetro de tipo genérico en una sola función.

Para parametrizar los tipos en una nueva función única, necesitamos nombrar el parámetro de tipo, al igual que lo hacemos para los parámetros de valor de una función. Puedes usar cualquier identificador como nombre de parámetro de tipo. Pero usaremos `T` porque, por convención, los nombres de parámetros de tipo en Rust son cortos, a menudo solo una letra, y la convención de nombrado de tipos de Rust es CamelCase. Corto para _tipo_, `T` es la elección predeterminada de la mayoría de los programadores de Rust.

Cuando usamos un parámetro en el cuerpo de la función, tenemos que declarar el nombre del parámetro en la firma para que el compilador sepa qué significa ese nombre. Del mismo modo, cuando usamos un nombre de parámetro de tipo en una firma de función, tenemos que declarar el nombre del parámetro de tipo antes de usarlo. Para definir la función genérica `largest`, colocamos las declaraciones de nombres de tipo dentro de corchetes angulares, `<>`, entre el nombre de la función y la lista de parámetros, así:

```rust
fn largest<T>(list: &[T]) -> &T {
```

Leemos esta definición como: la función `largest` es genérica sobre algún tipo `T`. Esta función tiene un parámetro llamado `list`, que es un slice de valores del tipo `T`. La función `largest` devolverá una referencia a un valor del mismo tipo `T`.

La Lista 10-5 muestra la definición combinada de la función `largest` que utiliza el tipo de datos genérico en su firma. La lista también muestra cómo podemos llamar a la función con un slice de valores de `i32` o `char` valores. Tenga en cuenta que este código todavía no se compilará, pero lo corregiremos más adelante en este capítulo.

Nombre de archivo: `src/main.rs`

```rust
fn largest<T>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

Lista 10-5: La función `largest` que utiliza parámetros de tipo genérico; esto todavía no se compila

Si compilamos este código ahora, obtendremos este error:

```bash
error[E0369]: binary operation `>` cannot be applied to type `&T`
 --> src/main.rs:5:17
  |
5 |         if item > largest {
  |            ---- ^ ------- &T
  |            |
  |            &T
  |
help: consider restricting type parameter `T`
  |
1 | fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
  |             ++++++++++++++++++++++
```

El texto de ayuda menciona `std::cmp::PartialOrd`, que es un _trait_, y vamos a hablar sobre traits en la siguiente sección. Por ahora, sabe que este error establece que el cuerpo de `largest` no funcionará para todos los posibles tipos que `T` podría ser. Debido a que queremos comparar valores del tipo `T` en el cuerpo, solo podemos usar tipos cuyos valores pueden ser ordenados. Para habilitar las comparaciones, la biblioteca estándar tiene el trait `std::cmp::PartialOrd` que se puede implementar en tipos (vea el Apéndice C para más información sobre este trait). Siguiendo la sugerencia del texto de ayuda, restringimos los tipos válidos para `T` solo a aquellos que implementan `PartialOrd` y este ejemplo se compilará, porque la biblioteca estándar implementa `PartialOrd` tanto en `i32` como en `char`.
