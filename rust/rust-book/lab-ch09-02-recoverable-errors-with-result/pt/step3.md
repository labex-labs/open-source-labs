# Alternativas ao Uso de match com Result\<T, E\>

Isso é muito `match`! A expressão `match` é muito útil, mas também muito primitiva. No Capítulo 13, você aprenderá sobre closures (fechamentos), que são usados com muitos dos métodos definidos em `Result<T, E>`. Esses métodos podem ser mais concisos do que usar `match` ao lidar com valores `Result<T, E>` em seu código.

Por exemplo, aqui está outra maneira de escrever a mesma lógica mostrada no Listing 9-5, desta vez usando closures e o método `unwrap_or_else`:

    // src/main.rs
    use std::fs::File;
    use std::io::ErrorKind;

    fn main() {
        let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
            if error.kind() == ErrorKind::NotFound {
                File::create("hello.txt").unwrap_or_else(|error| {
                    panic!("Problem creating the file: {:?}", error);
                })
            } else {
                panic!("Problem opening the file: {:?}", error);
            }
        });
    }

Embora este código tenha o mesmo comportamento do Listing 9-5, ele não contém nenhuma expressão `match` e é mais limpo de ler. Volte a este exemplo depois de ler o Capítulo 13 e procure o método `unwrap_or_else` na documentação da biblioteca padrão. Muitos mais desses métodos podem limpar enormes expressões `match` aninhadas quando você está lidando com erros.
