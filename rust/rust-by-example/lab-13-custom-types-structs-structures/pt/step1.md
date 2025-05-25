# Estruturas

Existem três tipos de estruturas ("structs") que podem ser criadas usando a palavra-chave `struct`:

- Tuple structs, que são, basicamente, tuplas nomeadas.
- As classic C structs
- Unit structs, que não possuem campos, são úteis para genéricos.

```rust
// Um atributo para esconder avisos de código não utilizado.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// Uma unit struct
struct Unit;

// Uma tuple struct
struct Pair(i32, f32);

// Uma struct com dois campos
struct Point {
    x: f32,
    y: f32,
}

// Structs podem ser reutilizadas como campos de outra struct
struct Rectangle {
    // Um retângulo pode ser especificado por onde os cantos superior esquerdo e inferior direito
    // estão no espaço.
    top_left: Point,
    bottom_right: Point,
}

fn main() {
    // Cria struct com field init shorthand
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // Imprime struct de debug
    println!("{:?}", peter);

    // Instancia um `Point`
    let point: Point = Point { x: 10.3, y: 0.4 };

    // Acessa os campos do ponto
    println!("point coordinates: ({}, {})", point.x, point.y);

    // Cria um novo ponto usando a sintaxe de atualização de struct para usar os campos do nosso
    // outro
    let bottom_right = Point { x: 5.2, ..point };

    // `bottom_right.y` será o mesmo que `point.y` porque usamos esse campo
    // de `point`
    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    // Desestrutura o ponto usando uma ligação `let`
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // a instanciação de struct também é uma expressão
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // Instancia uma unit struct
    let _unit = Unit;

    // Instancia uma tuple struct
    let pair = Pair(1, 0.1);

    // Acessa os campos de uma tuple struct
    println!("pair contains {:?} and {:?}", pair.0, pair.1);

    // Desestrutura uma tuple struct
    let Pair(integer, decimal) = pair;

    println!("pair contains {:?} and {:?}", integer, decimal);
}
```

## Atividade

1.  Adicione uma função `rect_area` que calcula a área de um `Rectangle` (tente usar desestruturação aninhada).
2.  Adicione uma função `square` que recebe um `Point` e um `f32` como argumentos e retorna um `Rectangle` com seu canto superior esquerdo no ponto e uma largura e altura correspondentes ao `f32`.
