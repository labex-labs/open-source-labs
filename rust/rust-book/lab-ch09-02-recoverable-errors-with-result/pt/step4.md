# Atalhos para Panic em Caso de Erro: unwrap e expect

Usar `match` funciona bem o suficiente, mas pode ser um pouco verboso e nem sempre comunica a intenção de forma clara. O tipo `Result<T, E>` tem muitos métodos auxiliares definidos nele para realizar várias tarefas mais específicas. O método `unwrap` é um método de atalho implementado exatamente como a expressão `match` que escrevemos no Listing 9-4. Se o valor `Result` for a variante `Ok`, `unwrap` retornará o valor dentro do `Ok`. Se o `Result` for a variante `Err`, `unwrap` chamará a macro `panic!` para nós. Aqui está um exemplo de `unwrap` em ação:

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

Se executarmos este código sem um arquivo _hello.txt_, veremos uma mensagem de erro da chamada `panic!` que o método `unwrap` faz:

    thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:4:49

Da mesma forma, o método `expect` também nos permite escolher a mensagem de erro `panic!`. Usar `expect` em vez de `unwrap` e fornecer boas mensagens de erro pode transmitir sua intenção e facilitar o rastreamento da origem de um panic. A sintaxe de `expect` é assim:

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
        .expect("hello.txt should be included in this project");
}
```

Usamos `expect` da mesma forma que `unwrap`: para retornar o manipulador do arquivo ou chamar a macro `panic!`. A mensagem de erro usada por `expect` em sua chamada para `panic!` será o parâmetro que passamos para `expect`, em vez da mensagem `panic!` padrão que `unwrap` usa. Veja como fica:

    thread 'main' panicked at 'hello.txt should be included in this project: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:5:10

Em código de qualidade de produção, a maioria dos Rustaceans escolhe `expect` em vez de `unwrap` e fornece mais contexto sobre o porquê da operação ser esperada para sempre ter sucesso. Dessa forma, se suas suposições forem provadas erradas, você terá mais informações para usar na depuração.
