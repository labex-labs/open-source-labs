# Variáveis e Mutabilidade

Como mencionado em "Armazenando Valores com Variáveis", por padrão, as variáveis são imutáveis. Este é um dos muitos incentivos que o Rust oferece para que você escreva seu código de uma forma que aproveite a segurança e a fácil concorrência que o Rust oferece. No entanto, você ainda tem a opção de tornar suas variáveis mutáveis. Vamos explorar como e por que o Rust o incentiva a favorecer a imutabilidade e por que, às vezes, você pode querer optar por não usá-la.

Quando uma variável é imutável, uma vez que um valor é vinculado a um nome, você não pode alterar esse valor. Para ilustrar isso, gere um novo projeto chamado _variables_ em seu diretório `project` usando `cargo new variables`.

Em seguida, em seu novo diretório `variables`, abra `src/main.rs` e substitua seu código pelo seguinte código, que ainda não compilará:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

Salve e execute o programa usando `cargo run`. Você deve receber uma mensagem de erro sobre um erro de imutabilidade, conforme mostrado nesta saída:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0384]: cannot assign twice to immutable variable `x`
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
3 |     println!("The value of x is: {x}");
4 |     x = 6;
  |     ^^^^^ cannot assign twice to immutable variable
```

Este exemplo mostra como o compilador ajuda você a encontrar erros em seus programas. Os erros do compilador podem ser frustrantes, mas na verdade eles apenas significam que seu programa não está fazendo com segurança o que você deseja que ele faça; eles _não_ significam que você não é um bom programador! Rustaceans experientes ainda recebem erros do compilador.

Você recebeu a mensagem de erro `cannot assign twice to immutable variable`x``porque tentou atribuir um segundo valor à variável imutável`x`.

É importante que obtenhamos erros em tempo de compilação quando tentamos alterar um valor que é designado como imutável, porque essa situação pode levar a bugs. Se uma parte do nosso código opera com a suposição de que um valor nunca mudará e outra parte do nosso código altera esse valor, é possível que a primeira parte do código não faça o que foi projetado para fazer. A causa desse tipo de bug pode ser difícil de rastrear depois, especialmente quando a segunda parte do código altera o valor apenas _às vezes_. O compilador Rust garante que, quando você afirma que um valor não mudará, ele realmente não mudará, então você não precisa controlá-lo sozinho. Seu código é, portanto, mais fácil de raciocinar.

Mas a mutabilidade pode ser muito útil e pode tornar o código mais conveniente de escrever. Embora as variáveis sejam imutáveis por padrão, você pode torná-las mutáveis adicionando `mut` na frente do nome da variável, como você fez no Capítulo 2. Adicionar `mut` também transmite a intenção aos futuros leitores do código, indicando que outras partes do código alterarão o valor desta variável.

Por exemplo, vamos alterar `src/main.rs` para o seguinte:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

Quando executamos o programa agora, obtemos isto:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/variables`
The value of x is: 5
The value of x is: 6
```

Podemos alterar o valor vinculado a `x` de `5` para `6` quando `mut` é usado. Em última análise, decidir se usa ou não a mutabilidade depende de você e do que você acha mais claro naquela situação específica.
