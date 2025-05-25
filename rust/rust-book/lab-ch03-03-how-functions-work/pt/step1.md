# Funções

As funções são predominantes no código Rust. Você já viu uma das funções mais importantes na linguagem: a função `main`, que é o ponto de entrada de muitos programas. Você também já viu a palavra-chave `fn`, que permite declarar novas funções.

Crie um novo projeto chamado `functions`:

```bash
cargo new functions
cd functions
```

O código Rust usa _snake case_ como o estilo convencional para nomes de funções e variáveis, no qual todas as letras são minúsculas e sublinhados separam as palavras. Aqui está um programa que contém um exemplo de definição de função:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

Definimos uma função em Rust inserindo `fn` seguido por um nome de função e um conjunto de parênteses. As chaves dizem ao compilador onde o corpo da função começa e termina.

Podemos chamar qualquer função que definimos inserindo seu nome seguido por um conjunto de parênteses. Como `another_function` é definida no programa, ela pode ser chamada de dentro da função `main`. Observe que definimos `another_function` _depois_ da função `main` no código-fonte; poderíamos tê-la definido antes também. Rust não se importa onde você define suas funções, apenas que elas sejam definidas em algum lugar em um escopo que possa ser visto pelo chamador.

Vamos iniciar um novo projeto binário chamado _functions_ para explorar as funções mais a fundo. Coloque o exemplo `another_function` em `src/main.rs` e execute-o. Você deve ver a seguinte saída:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.28s
     Running `target/debug/functions`
Hello, world!
Another function.
```

As linhas são executadas na ordem em que aparecem na função `main`. Primeiro, a mensagem "Hello, world!" é impressa, e então `another_function` é chamada e sua mensagem é impressa.
