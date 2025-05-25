# Um Programa de Exemplo Usando Structs

Para entender quando podemos querer usar structs, vamos escrever um programa que calcula a área de um retângulo. Começaremos usando variáveis individuais e, em seguida, refatoraremos o programa até usarmos structs.

Vamos criar um novo projeto binário com o Cargo chamado _rectangles_ que receberá a largura e a altura de um retângulo especificados em pixels e calculará a área do retângulo. A Listagem 5-8 mostra um programa curto com uma maneira de fazer exatamente isso no `src/main.rs` do nosso projeto.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "The area of the rectangle is {} square pixels.",
        area(width1, height1)
    );
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}
```

Listagem 5-8: Calculando a área de um retângulo especificado por variáveis separadas de largura e altura

Agora, execute este programa usando `cargo run`:

```rust
The area of the rectangle is 1500 square pixels.
```

Este código consegue descobrir a área do retângulo chamando a função `area` com cada dimensão, mas podemos fazer mais para tornar este código claro e legível.

O problema com este código é evidente na assinatura de `area`:

```rust
fn area(width: u32, height: u32) -> u32 {
```

A função `area` deve calcular a área de um retângulo, mas a função que escrevemos tem dois parâmetros, e não está claro em nenhum lugar do nosso programa que os parâmetros estão relacionados. Seria mais legível e mais gerenciável agrupar largura e altura. Já discutimos uma maneira de fazer isso em "O Tipo Tupla": usando tuplas.
