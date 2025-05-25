# Partes Restantes de um Valor com ..

Com valores que têm muitas partes, podemos usar a sintaxe `..` para usar partes específicas e ignorar o restante, evitando a necessidade de listar sublinhados para cada valor ignorado. O padrão `..` ignora quaisquer partes de um valor que não tenhamos correspondido explicitamente no restante do padrão. Na Listagem 18-23, temos uma struct `Point` que contém uma coordenada no espaço tridimensional. Na expressão `match`, queremos operar apenas na coordenada `x` e ignorar os valores nos campos `y` e `z`.

Nome do arquivo: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
    z: i32,
}

let origin = Point { x: 0, y: 0, z: 0 };

match origin {
    Point { x, .. } => println!("x is {x}"),
}
```

Listagem 18-23: Ignorando todos os campos de um `Point` exceto `x` usando `..`

Listamos o valor `x` e, em seguida, apenas incluímos o padrão `..`. Isso é mais rápido do que ter que listar `y: _` e `z: _`, particularmente quando estamos trabalhando com structs que têm muitos campos em situações em que apenas um ou dois campos são relevantes.

A sintaxe `..` se expandirá para quantos valores forem necessários. A Listagem 18-24 mostra como usar `..` com uma tupla.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (first, .., last) => {
            println!("Some numbers: {first}, {last}");
        }
    }
}
```

Listagem 18-24: Correspondendo apenas aos primeiros e últimos valores em uma tupla e ignorando todos os outros valores

Neste código, os primeiros e últimos valores são correspondidos com `first` e `last`. O `..` corresponderá e ignorará tudo no meio.

No entanto, usar `..` deve ser inequívoco. Se não estiver claro quais valores se destinam à correspondência e quais devem ser ignorados, o Rust nos dará um erro. A Listagem 18-25 mostra um exemplo de uso ambíguo de `..`, portanto, não compilará.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (.., second, ..) => {
            println!("Some numbers: {second}");
        },
    }
}
```

Listagem 18-25: Uma tentativa de usar `..` de forma ambígua

Quando compilamos este exemplo, recebemos este erro:

```bash
error: `..` can only be used once per tuple pattern
 --> src/main.rs:5:22
  |
5 |         (.., second, ..) => {
  |          --          ^^ can only be used once per tuple pattern
  |          |
  |          previously used here
```

É impossível para o Rust determinar quantos valores na tupla ignorar antes de corresponder a um valor com `second` e, em seguida, quantos valores adicionais ignorar depois disso. Este código pode significar que queremos ignorar `2`, vincular `second` a `4` e, em seguida, ignorar `8`, `16` e `32`; ou que queremos ignorar `2` e `4`, vincular `second` a `8` e, em seguida, ignorar `16` e `32`; e assim por diante. O nome da variável `second` não significa nada de especial para o Rust, então recebemos um erro do compilador porque usar `..` em dois lugares como este é ambíguo.
