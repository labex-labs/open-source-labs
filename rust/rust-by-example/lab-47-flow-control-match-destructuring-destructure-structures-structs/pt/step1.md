# structs

Analogamente, uma `struct` pode ser desestruturada como mostrado:

```rust
fn main() {
    struct Foo {
        x: (u32, u32),
        y: u32,
    }

    // Tente alterar os valores na estrutura para ver o que acontece
    let foo = Foo { x: (1, 2), y: 3 };

    match foo {
        Foo { x: (1, b), y } => println!("O primeiro de x é 1, b = {},  y = {} ", b, y),

        // você pode desestruturar structs e renomear as variáveis,
        // a ordem não é importante
        Foo { y: 2, x: i } => println!("y é 2, i = {:?}", i),

        // e também pode ignorar algumas variáveis:
        Foo { y, .. } => println!("y = {}, não nos importamos com x", y),
        // isso dará um erro: o padrão não menciona o campo `x`
        //Foo { y } => println!("y = {}", y),
    }

    let faa = Foo { x: (1, 2), y: 3 };

    // Você não precisa de um bloco match para desestruturar structs:
    let Foo { x : x0, y: y0 } = faa;
    println!("Fora: x0 = {x0:?}, y0 = {y0}");
}
```
