# Configurando um Novo Projeto

Para configurar um novo projeto, vá para o diretório `project` que você criou no Capítulo 1 e crie um novo projeto usando o Cargo, da seguinte forma:

```bash
cargo new guessing_game
cd guessing_game
```

O primeiro comando, `cargo new`, recebe o nome do projeto (`guessing_game`) como o primeiro argumento. O segundo comando muda para o diretório do novo projeto.

Observe o arquivo `Cargo.toml` gerado:

Nome do arquivo: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at
https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

Como você viu no Capítulo 1, `cargo new` gera um programa "Olá, mundo!" para você. Verifique o arquivo `src/main.rs`:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Agora, vamos compilar este programa "Olá, mundo!" e executá-lo na mesma etapa usando o comando `cargo run`:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Hello, world!
```

O comando `run` é útil quando você precisa iterar rapidamente em um projeto, como faremos neste jogo, testando rapidamente cada iteração antes de passar para a próxima.

Reabra o arquivo `src/main.rs`. Você escreverá todo o código neste arquivo.
