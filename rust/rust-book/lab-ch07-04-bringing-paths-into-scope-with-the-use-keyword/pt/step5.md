# Usando Pacotes Externos

No Capítulo 2, programamos um projeto de jogo de adivinhação que usava um pacote externo chamado `rand` para obter números aleatórios. Para usar `rand` em nosso projeto, adicionamos esta linha ao `Cargo.toml`:

Nome do arquivo: `Cargo.toml`

```tomltoml
rand = "0.8.5"
```

Adicionar `rand` como uma dependência em `Cargo.toml` diz ao Cargo para baixar o pacote `rand` e quaisquer dependências de *https://crates.io*, e tornar `rand` disponível para nosso projeto.

Então, para trazer as definições de `rand` para o escopo do nosso pacote, adicionamos uma linha `use` começando com o nome do crate, `rand`, e listamos os itens que queríamos trazer para o escopo. Recorde que em "Gerando um Número Aleatório", trouxemos o trait `Rng` para o escopo e chamamos a função `rand::thread_rng`:

```rust
use rand::Rng;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=100);
}
```

Membros da comunidade Rust disponibilizaram muitos pacotes em *https://crates.io*, e puxar qualquer um deles para seu pacote envolve as mesmas etapas: listá-los no arquivo `Cargo.toml` do seu pacote e usar `use` para trazer itens de seus crates para o escopo.

Observe que a biblioteca padrão `std` também é um crate que é externo ao nosso pacote. Como a biblioteca padrão é fornecida com a linguagem Rust, não precisamos alterar `Cargo.toml` para incluir `std`. Mas precisamos nos referir a ela com `use` para trazer itens de lá para o escopo do nosso pacote. Por exemplo, com `HashMap` usaríamos esta linha:

```rust
use std::collections::HashMap;
```

Este é um caminho absoluto começando com `std`, o nome do crate da biblioteca padrão.
