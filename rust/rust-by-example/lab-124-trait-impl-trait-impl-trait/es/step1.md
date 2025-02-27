# `impl Trait`

`impl Trait` se puede utilizar en dos ubicaciones:

1.  como un tipo de argumento
2.  como un tipo de retorno

## Como un tipo de argumento

Si su función es genérica sobre un trato pero no le importa el tipo específico, puede simplificar la declaración de la función utilizando `impl Trait` como el tipo del argumento.

Por ejemplo, considere el siguiente código:

```rust
fn parse_csv_document<R: std::io::BufRead>(src: R) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // Para cada línea en la fuente
            line.map(|line| {
                // Si la línea se leyó correctamente, procesarla, si no, devolver el error
                line.split(',') // Dividir la línea separada por comas
                 .map(|entry| String::from(entry.trim())) // Quitar los espacios en blanco al principio y al final
                 .collect() // Recopilar todas las cadenas en una fila en un Vec<String>
            })
        })
     .collect() // Recopilar todas las líneas en un Vec<Vec<String>>
}
```

`parse_csv_document` es genérica, lo que le permite tomar cualquier tipo que implemente BufRead, como `BufReader<File>` o `[u8]`, pero no es importante de qué tipo es `R`, y `R` solo se utiliza para declarar el tipo de `src`, por lo que la función también se puede escribir como:

```rust
fn parse_csv_document(src: impl std::io::BufRead) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // Para cada línea en la fuente
            line.map(|line| {
                // Si la línea se leyó correctamente, procesarla, si no, devolver el error
                line.split(',') // Dividir la línea separada por comas
                 .map(|entry| String::from(entry.trim())) // Quitar los espacios en blanco al principio y al final
                 .collect() // Recopilar todas las cadenas en una fila en un Vec<String>
            })
        })
     .collect() // Recopilar todas las líneas en un Vec<Vec<String>>
}
```

Tenga en cuenta que utilizar `impl Trait` como un tipo de argumento significa que no puede declarar explícitamente qué forma de la función utiliza, es decir, `parse_csv_document::<std::io::Empty>(std::io::empty())` no funcionará con el segundo ejemplo.

## Como un tipo de retorno

Si su función devuelve un tipo que implementa `MyTrait`, puede escribir su tipo de retorno como `-> impl MyTrait`. Esto puede ayudar a simplificar sus firmas de tipo en gran medida.

```rust
use std::iter;
use std::vec::IntoIter;

// Esta función combina dos `Vec<i32>` y devuelve un iterador sobre él.
// Mira lo complicado que es su tipo de retorno!
fn combine_vecs_explicit_return_type(
    v: Vec<i32>,
    u: Vec<i32>,
) -> iter::Cycle<iter::Chain<IntoIter<i32>, IntoIter<i32>>> {
    v.into_iter().chain(u.into_iter()).cycle()
}

// Esta es exactamente la misma función, pero su tipo de retorno utiliza `impl Trait`.
// Mira lo mucho más simple que es!
fn combine_vecs(
    v: Vec<i32>,
    u: Vec<i32>,
) -> impl Iterator<Item=i32> {
    v.into_iter().chain(u.into_iter()).cycle()
}

fn main() {
    let v1 = vec![1, 2, 3];
    let v2 = vec![4, 5];
    let mut v3 = combine_vecs(v1, v2);
    assert_eq!(Some(1), v3.next());
    assert_eq!(Some(2), v3.next());
    assert_eq!(Some(3), v3.next());
    assert_eq!(Some(4), v3.next());
    assert_eq!(Some(5), v3.next());
    println!("todo hecho");
}
```

Más importante aún, algunos tipos de Rust no se pueden escribir. Por ejemplo, cada clausura tiene su propio tipo concreto sin nombre. Antes de la sintaxis `impl Trait`, tenía que asignar memoria en el montón para devolver una clausura. Pero ahora puede hacerlo todo de forma estática, así:

```rust
// Devuelve una función que suma `y` a su entrada
fn make_adder_function(y: i32) -> impl Fn(i32) -> i32 {
    let closure = move |x: i32| { x + y };
    closure
}

fn main() {
    let plus_one = make_adder_function(1);
    assert_eq!(plus_one(2), 3);
}
```

También puede utilizar `impl Trait` para devolver un iterador que utiliza clausuras `map` o `filter`! Esto hace que sea más fácil utilizar `map` y `filter`. Debido a que los tipos de clausura no tienen nombres, no puede escribir un tipo de retorno explícito si su función devuelve iteradores con clausuras. Pero con `impl Trait` puede hacer esto fácilmente:

```rust
fn double_positives<'a>(numbers: &'a Vec<i32>) -> impl Iterator<Item = i32> + 'a {
    numbers
     .iter()
     .filter(|x| x > &&0)
     .map(|x| x * 2)
}

fn main() {
    let singles = vec![-3, -2, 2, 3];
    let doubles = double_positives(&singles);
    assert_eq!(doubles.collect::<Vec<i32>>(), vec![4, 6]);
}
```
