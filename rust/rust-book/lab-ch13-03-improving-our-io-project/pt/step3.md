# Usando o Iterador Retornado Diretamente

Abra o arquivo `src/main.rs` do seu projeto I/O, que deve ter esta aparência:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    --snip--
}
```

Primeiro, vamos alterar o início da função `main` que tínhamos na Listagem 12-24 para o código na Listagem 13-18, que desta vez usa um iterador. Isso não compilará até que também atualizemos `Config::build`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let config =
        Config::build(env::args()).unwrap_or_else(|err| {
            eprintln!("Problem parsing arguments: {err}");
            process::exit(1);
        });

    --snip--
}
```

Listagem 13-18: Passando o valor de retorno de `env::args` para `Config::build`

A função `env::args` retorna um iterador! Em vez de coletar os valores do iterador em um vetor e, em seguida, passar uma fatia para `Config::build`, agora estamos passando a propriedade do iterador retornado de `env::args` para `Config::build` diretamente.

Em seguida, precisamos atualizar a definição de `Config::build`. No arquivo `src/lib.rs` do seu projeto I/O, vamos alterar a assinatura de `Config::build` para se parecer com a Listagem 13-19. Isso ainda não compilará, porque precisamos atualizar o corpo da função.

Nome do arquivo: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        --snip--
```

Listagem 13-19: Atualizando a assinatura de `Config::build` para esperar um iterador

A documentação da biblioteca padrão para a função `env::args` mostra que o tipo do iterador que ela retorna é `std::env::Args`, e esse tipo implementa o trait `Iterator` e retorna valores `String`.

Atualizamos a assinatura da função `Config::build` para que o parâmetro `args` tenha um tipo genérico com as restrições de trait `impl Iterator<Item = String>` em vez de `&[String]`. Este uso da sintaxe `impl Trait` que discutimos em "Traits como Parâmetros" significa que `args` pode ser qualquer tipo que implemente o tipo `Iterator` e retorne itens `String`.

Como estamos assumindo a propriedade de `args` e vamos mutar `args` iterando sobre ele, podemos adicionar a palavra-chave `mut` na especificação do parâmetro `args` para torná-lo mutável.
