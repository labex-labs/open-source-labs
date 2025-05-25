# Retornando Erros da Função run

Com a lógica restante do programa separada na função `run`, podemos melhorar o tratamento de erros, como fizemos com `Config::build` na Listagem 12-9. Em vez de permitir que o programa entre em pânico chamando `expect`, a função `run` retornará um `Result<T, E>` quando algo der errado. Isso nos permitirá consolidar ainda mais a lógica em torno do tratamento de erros em `main` de uma forma amigável ao usuário. A Listagem 12-12 mostra as alterações que precisamos fazer na assinatura e no corpo de `run`.

Nome do arquivo: `src/main.rs`

```rust
1 use std::error::Error;

--snip--

2 fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)3 ?;

    println!("With text:\n{contents}");

  4 Ok(())
}
```

Listagem 12-12: Alterando a função `run` para retornar `Result`

Fizemos três alterações significativas aqui. Primeiro, alteramos o tipo de retorno da função `run` para `Result<(), Box<dyn Error>>` \[2]. Esta função anteriormente retornava o tipo unitário, `()`, e mantemos isso como o valor retornado no caso `Ok`.

Para o tipo de erro, usamos o _objeto trait_ `Box<dyn Error>` (e trouxemos `std::error::Error` para o escopo com uma instrução `use` no topo \[1]). Abordaremos objetos trait no Capítulo 17. Por enquanto, apenas saiba que `Box<dyn Error>` significa que a função retornará um tipo que implementa o trait `Error`, mas não precisamos especificar qual tipo específico será o valor de retorno. Isso nos dá flexibilidade para retornar valores de erro que podem ser de tipos diferentes em diferentes casos de erro. A palavra-chave `dyn` é abreviação de _dynamic_ (dinâmico).

Segundo, removemos a chamada para `expect` em favor do operador `?` \[3], como falamos no Capítulo 9. Em vez de `panic!` em um erro, `?` retornará o valor do erro da função atual para o chamador lidar.

Terceiro, a função `run` agora retorna um valor `Ok` no caso de sucesso \[4]. Declaramos o tipo de sucesso da função `run` como `()` na assinatura, o que significa que precisamos encapsular o valor do tipo unitário no valor `Ok`. Esta sintaxe `Ok(())` pode parecer um pouco estranha no início, mas usar `()` assim é a maneira idiomática de indicar que estamos chamando `run` apenas por seus efeitos colaterais; ela não retorna um valor que precisamos.

Quando você executar este código, ele compilará, mas exibirá um aviso:

    warning: unused `Result` that must be used
      --> src/main.rs:19:5
       |
    19 |     run(config);
       |     ^^^^^^^^^^^^
       |
       = note: `#[warn(unused_must_use)]` on by default
       = note: this `Result` may be an `Err` variant, which should be
    handled

Rust nos diz que nosso código ignorou o valor `Result` e o valor `Result` pode indicar que um erro ocorreu. Mas não estamos verificando se houve ou não um erro, e o compilador nos lembra que provavelmente queríamos ter algum código de tratamento de erros aqui! Vamos corrigir esse problema agora.
