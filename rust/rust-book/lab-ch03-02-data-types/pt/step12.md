# Acesso Inválido a Elemento de Array

Vamos ver o que acontece se você tentar acessar um elemento de um array que está além do final do array. Digamos que você execute este código, semelhante ao jogo de adivinhação no Capítulo 2, para obter um índice de array do usuário:

Nome do arquivo: `src/main.rs`

```rust
use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    println!("Por favor, insira um índice de array.");

    let mut index = String::new();

    io::stdin()
        .read_line(&mut index)
        .expect("Falha ao ler a linha");

    let index: usize = index
        .trim()
        .parse()
        .expect("O índice inserido não era um número");

    let element = a[index];

    println!(
        "O valor do elemento no índice {index} é: {element}"
    );
}
```

Este código compila com sucesso. Se você executar este código usando `cargo run` e inserir `0`, `1`, `2`, `3` ou `4`, o programa imprimirá o valor correspondente naquele índice no array. Se, em vez disso, você inserir um número além do final do array, como `10`, verá uma saída como esta:

    thread 'main' panicked at 'index out of bounds: the len is 5 but the index is
    10', src/main.rs:19:19
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

O programa resultou em um erro de _tempo de execução_ (runtime) no ponto de uso de um valor inválido na operação de indexação. O programa saiu com uma mensagem de erro e não executou a instrução `println!` final. Quando você tenta acessar um elemento usando indexação, o Rust verificará se o índice que você especificou é menor que o comprimento do array. Se o índice for maior ou igual ao comprimento, o Rust entrará em pânico. Essa verificação precisa acontecer em tempo de execução, especialmente neste caso, porque o compilador não pode saber qual valor um usuário inserirá quando executar o código mais tarde.

Este é um exemplo dos princípios de segurança de memória do Rust em ação. Em muitas linguagens de baixo nível, esse kind de verificação não é feito, e quando você fornece um índice incorreto, memória inválida pode ser acessada. O Rust protege você contra esse tipo de erro saindo imediatamente em vez de permitir o acesso à memória e continuar. O Capítulo 9 discute mais sobre o tratamento de erros do Rust e como você pode escrever código legível e seguro que não entre em pânico nem permita acesso inválido à memória.
