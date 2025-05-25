# Desestruturando Enums (Destructuring Enums)

Nós desestruturamos enums neste livro (por exemplo, na Listagem 6-5), mas ainda não discutimos explicitamente que o padrão para desestruturar um enum corresponde à maneira como os dados armazenados dentro do enum são definidos. Como exemplo, na Listagem 18-15, usamos o enum `Message` da Listagem 6-2 e escrevemos um `match` com padrões que desestruturarão cada valor interno.

Nome do arquivo: `src/main.rs`

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
  1 let msg = Message::ChangeColor(0, 160, 255);

    match msg {
      2 Message::Quit => {
            println!(
                "The Quit variant has no data to destructure."
            );
        }
      3 Message::Move { x, y } => {
            println!(
                "Move in the x dir {x}, in the y dir {y}"
            );
        }
      4 Message::Write(text) => {
            println!("Text message: {text}");
        }
      5 Message::ChangeColor(r, g, b) => println!(
            "Change color to red {r}, green {g}, and blue {b}"
        ),
    }
}
```

Listagem 18-15: Desestruturando variantes de enum que contêm diferentes tipos de valores

Este código imprimirá `Change color to red 0, green 160, and blue 255`. Tente alterar o valor de `msg` \[1] para ver o código dos outros braços sendo executado.

Para variantes de enum sem nenhum dado, como `Message::Quit` \[2], não podemos desestruturar o valor ainda mais. Só podemos corresponder ao valor literal `Message::Quit`, e nenhuma variável está nesse padrão.

Para variantes de enum semelhantes a structs, como `Message::Move` \[3], podemos usar um padrão semelhante ao padrão que especificamos para corresponder a structs. Após o nome da variante, colocamos chaves e, em seguida, listamos os campos com variáveis para quebrar as partes para usar no código para este braço. Aqui, usamos a forma abreviada como fizemos na Listagem 18-13.

Para variantes de enum semelhantes a tuplas, como `Message::Write` que contém uma tupla com um elemento \[4] e `Message::ChangeColor` que contém uma tupla com três elementos \[5], o padrão é semelhante ao padrão que especificamos para corresponder a tuplas. O número de variáveis no padrão deve corresponder ao número de elementos na variante que estamos correspondendo.
