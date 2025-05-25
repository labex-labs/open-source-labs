# Criando um Construtor para Config

Até agora, extraímos a lógica responsável por analisar os argumentos da linha de comando de `main` e a colocamos na função `parse_config`. Fazer isso nos ajudou a ver que os valores `query` e `file_path` estavam relacionados, e essa relação deve ser transmitida em nosso código. Em seguida, adicionamos uma struct `Config` para nomear o propósito relacionado de `query` e `file_path` e para poder retornar os nomes dos valores como nomes de campos de struct da função `parse_config`.

Então, agora que o propósito da função `parse_config` é criar uma instância `Config`, podemos mudar `parse_config` de uma função simples para uma função chamada `new` que está associada à struct `Config`. Fazer essa alteração tornará o código mais idiomático. Podemos criar instâncias de tipos na biblioteca padrão, como `String`, chamando `String::new`. Da mesma forma, mudando `parse_config` para uma função `new` associada a `Config`, poderemos criar instâncias de `Config` chamando `Config::new`. A Listagem 12-7 mostra as alterações que precisamos fazer.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

Listagem 12-7: Mudando `parse_config` para `Config::new`

Atualizamos `main` onde estávamos chamando `parse_config` para, em vez disso, chamar `Config::new` \[1]. Mudamos o nome de `parse_config` para `new` \[3] e o movemos dentro de um bloco `impl` \[2], que associa a função `new` a `Config`. Tente compilar este código novamente para garantir que ele funcione.
