# `impl Trait`

`impl Trait` pode ser usado em dois locais:

1.  como um tipo de argumento
2.  como um tipo de retorno

## Como um tipo de argumento

Se sua função é genérica sobre um trait (característica), mas você não se importa com o tipo específico, você pode simplificar a declaração da função usando `impl Trait` como o tipo do argumento.

Por exemplo, considere o seguinte código:

```rust
fn parse_csv_document<R: std::io::BufRead>(src: R) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
        .map(|line| {
            // For each line in the source
            line.map(|line| {
                // If the line was read successfully, process it, if not, return the error
                line.split(',') // Split the line separated by commas
                    .map(|entry| String::from(entry.trim())) // Remove leading and trailing whitespace
                    .collect() // Collect all strings in a row into a Vec<String>
            })
        })
        .collect() // Collect all lines into a Vec<Vec<String>>
}
```

`parse_csv_document` é genérica, permitindo que ela aceite qualquer tipo que implemente `BufRead`, como `BufReader<File>` ou `[u8]`, mas não é importante qual tipo `R` é, e `R` é usado apenas para declarar o tipo de `src`, então a função também pode ser escrita como:

```rust
fn parse_csv_document(src: impl std::io::BufRead) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
        .map(|line| {
            // For each line in the source
            line.map(|line| {
                // If the line was read successfully, process it, if not, return the error
                line.split(',') // Split the line separated by commas
                    .map(|entry| String::from(entry.trim())) // Remove leading and trailing whitespace
                    .collect() // Collect all strings in a row into a Vec<String>
            })
        })
        .collect() // Collect all lines into a Vec<Vec<String>>
}
```

Observe que usar `impl Trait` como um tipo de argumento significa que você não pode declarar explicitamente qual forma da função você usa, ou seja, `parse_csv_document::<std::io::Empty>(std::io::empty())` não funcionará com o segundo exemplo.

## Como um tipo de retorno

Se sua função retorna um tipo que implementa `MyTrait`, você pode escrever seu tipo de retorno como `-> impl MyTrait`. Isso pode ajudar a simplificar suas assinaturas de tipo bastante!

```rust
use std::iter;
use std::vec::IntoIter;

// This function combines two `Vec<i32>` and returns an iterator over it.
// Look how complicated its return type is!
fn combine_vecs_explicit_return_type(
    v: Vec<i32>,
    u: Vec<i32>,
) -> iter::Cycle<iter::Chain<IntoIter<i32>, IntoIter<i32>>> {
    v.into_iter().chain(u.into_iter()).cycle()
}

// This is the exact same function, but its return type uses `impl Trait`.
// Look how much simpler it is!
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
    println!("all done");
}
```

Mais importante, alguns tipos Rust não podem ser escritos. Por exemplo, cada closure (fechamento) tem seu próprio tipo concreto sem nome. Antes da sintaxe `impl Trait`, você tinha que alocar no heap (pilha) para retornar um closure. Mas agora você pode fazer tudo estaticamente, assim:

```rust
// Returns a function that adds `y` to its input
fn make_adder_function(y: i32) -> impl Fn(i32) -> i32 {
    let closure = move |x: i32| { x + y };
    closure
}

fn main() {
    let plus_one = make_adder_function(1);
    assert_eq!(plus_one(2), 3);
}
```

Você também pode usar `impl Trait` para retornar um iterator que usa closures `map` ou `filter`! Isso torna o uso de `map` e `filter` mais fácil. Como os tipos de closure não têm nomes, você não pode escrever um tipo de retorno explícito se sua função retornar iteradores com closures. Mas com `impl Trait` você pode fazer isso facilmente:

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
