# Dividindo o Código em uma Crate de Biblioteca

Nosso projeto `minigrep` está com uma boa aparência até agora! Agora, vamos dividir o arquivo `src/main.rs` e colocar algum código no arquivo `src/lib.rs`. Dessa forma, podemos testar o código e ter um arquivo `src/main.rs` com menos responsabilidades.

Vamos mover todo o código que não está na função `main` de `src/main.rs` para `src/lib.rs`:

- A definição da função `run`
- As instruções `use` relevantes
- A definição de `Config`
- A definição da função `Config::build`

O conteúdo de `src/lib.rs` deve ter as assinaturas mostradas na Listagem 12-13 (omitimos os corpos das funções para brevidade). Observe que isso não compilará até que modifiquemos `src/main.rs` na Listagem 12-14.

Nome do arquivo: `src/lib.rs`

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(
        args: &[String],
    ) -> Result<Config, &'static str> {
        --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    --snip--
}
```

Listagem 12-13: Movendo `Config` e `run` para `src/lib.rs`

Fizemos uso liberal da palavra-chave `pub`: em `Config`, em seus campos e em seu método `build`, e na função `run`. Agora temos uma crate de biblioteca que possui uma API pública que podemos testar!

Agora precisamos trazer o código que movemos para `src/lib.rs` para o escopo da crate binária em `src/main.rs`, conforme mostrado na Listagem 12-14.

Nome do arquivo: `src/main.rs`

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    --snip--
    if let Err(e) = minigrep::run(config) {
        --snip--
    }
}
```

Listagem 12-14: Usando a crate de biblioteca `minigrep` em `src/main.rs`

Adicionamos uma linha `use minigrep::Config` para trazer o tipo `Config` da crate de biblioteca para o escopo da crate binária, e prefixamos a função `run` com o nome da nossa crate. Agora toda a funcionalidade deve estar conectada e deve funcionar. Execute o programa com `cargo run` e certifique-se de que tudo está funcionando corretamente.

Ufa! Foi muito trabalho, mas nos preparamos para o sucesso no futuro. Agora é muito mais fácil lidar com erros, e tornamos o código mais modular. Quase todo o nosso trabalho será feito em `src/lib.rs` daqui em diante.

Vamos aproveitar essa nova modularidade fazendo algo que teria sido difícil com o código antigo, mas é fácil com o novo código: vamos escrever alguns testes!
