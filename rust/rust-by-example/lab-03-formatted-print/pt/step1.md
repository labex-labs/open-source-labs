# Impressão formatada

A impressão é tratada por uma série de `macros` definidas em `std::fmt`, algumas das quais incluem:

- `format!`: escreve texto formatado para `String`.
- `print!`: igual a `format!`, mas o texto é impresso no console (io::stdout).
- `println!`: igual a `print!`, mas uma nova linha é adicionada.
- `eprint!`: igual a `print!`, mas o texto é impresso no erro padrão (io::stderr).
- `eprintln!`: igual a `eprint!`, mas uma nova linha é adicionada.

Todas analisam o texto da mesma forma. Como vantagem, Rust verifica a correção da formatação em tempo de compilação.

```rust
fn main() {
    // Em geral, `{}` será automaticamente substituído por quaisquer
    // argumentos. Estes serão stringificados.
    println!("{} dias", 31);

    // Argumentos posicionais podem ser usados. Especificar um inteiro dentro de `{}`
    // determina qual argumento adicional será substituído. Os argumentos começam
    // em 0 imediatamente após a string de formatação.
    println!("{0}, isto é {1}. {1}, isto é {0}", "Alice", "Bob");

    // Assim como argumentos nomeados.
    println!("{subject} {verb} {object}",
             object="o cão preguiçoso",
             subject="a raposa marrom rápida",
             verb="pula sobre");

    // Diferentes formatações podem ser invocadas especificando o caractere de formatação
    // após um `:`.
    println!("Base 10:               {}",   69420); // 69420
    println!("Base 2 (binário):       {:b}", 69420); // 10000111100101100
    println!("Base 8 (octal):        {:o}", 69420); // 207454
    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c
    println!("Base 16 (hexadecimal): {:X}", 69420); // 10F2C

    // Você pode justificar o texto à direita com uma largura especificada. Isso irá
    // gerar "    1". (Quatro espaços em branco e um "1", para uma largura total de 5.)
    println!("{number:>5}", number=1);

    // Você pode preencher números com zeros extras,
    println!("{number:0>5}", number=1); // 00001
    // e justificar à esquerda invertendo o sinal. Isso gerará "10000".
    println!("{number:0<5}", number=1); // 10000

    // Você pode usar argumentos nomeados no especificador de formato anexando um `$`.
    println!("{number:0>width$}", number=1, width=5);

    // Rust ainda verifica para garantir que o número correto de argumentos seja usado.
    println!("Meu nome é {0}, {1} {0}", "Bond");
    // FIXME ^ Adicione o argumento ausente: "James"

    // Apenas tipos que implementam fmt::Display podem ser formatados com `{}`. Tipos definidos pelo usuário
    // não implementam fmt::Display por padrão.

    #[allow(dead_code)] // desabilita `dead_code` que avisa contra módulo não utilizado
    struct Structure(i32);

    // Isso não compilará porque `Structure` não implementa
    // fmt::Display.
    // println!("Esta struct `{}` não imprimirá...", Structure(3));
    // TODO ^ Tente descomentar esta linha

    // Para Rust 1.58 e superior, você pode capturar diretamente o argumento de uma
    // variável circundante. Assim como o acima, isso gerará
    // "    1", 4 espaços em branco e um "1".
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");
}
```

`std::fmt` contém muitas `traits` que governam a exibição do texto. A forma base de duas importantes está listada abaixo:

- `fmt::Debug`: Usa o marcador `{:?}`. Formata o texto para fins de _debugging_.
- `fmt::Display`: Usa o marcador `{}`. Formata o texto de uma maneira mais elegante e amigável ao usuário.

Aqui, usamos `fmt::Display` porque a biblioteca padrão fornece implementações para esses tipos. Para imprimir texto para tipos personalizados, mais etapas são necessárias.

Implementar a _trait_ `fmt::Display` implementa automaticamente a _trait_ `ToString`, que nos permite converter o tipo para `String`.

Na _linha 43_, `#[allow(dead_code)]` é um \[atributo] que se aplica apenas ao módulo após ele.

## Atividades

- Corrija o problema no código acima (veja FIXME) para que ele seja executado sem erros.
- Tente descomentar a linha que tenta formatar a struct `Structure` (veja TODO)
- Adicione uma chamada de macro `println!` que imprima: `Pi is roughly 3.142` controlando o número de casas decimais exibidas. Para os propósitos deste exercício, use `let pi = 3.141592` como uma estimativa para pi. (Dica: você pode precisar verificar a documentação `std::fmt` para definir o número de decimais a serem exibidos)
