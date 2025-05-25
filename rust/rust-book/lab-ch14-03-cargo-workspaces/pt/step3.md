# Criando o Segundo Pacote no Workspace

Em seguida, vamos criar outro pacote membro no workspace e chamá-lo de `add_one`. Altere o `Cargo.toml` de nível superior para especificar o caminho _add_one_ na lista `members`:

Nome do arquivo: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

Em seguida, gere um novo crate de biblioteca chamado `add_one`:

```bash
$ cargo new add_one --lib
Created library $(add_one) package
```

Seu diretório `add` agora deve ter esses diretórios e arquivos:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── add_one
    │   ├── Cargo.toml
    │   └── src
    │       └── lib.rs
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

No arquivo `add_one/src/lib.rs`, vamos adicionar uma função `add_one`:

Nome do arquivo: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

Agora podemos ter o pacote `adder` com nosso binário dependendo do pacote `add_one` que possui nossa biblioteca. Primeiro, precisaremos adicionar uma dependência de caminho em `add_one` para _adder/Cargo.toml_:

Nome do arquivo: `adder/Cargo.toml`

```tomlrust
[dependencies]
add_one = { path = "../add_one" }
```

O Cargo não assume que os crates em um workspace dependerão uns dos outros, então precisamos ser explícitos sobre as relações de dependência.

Em seguida, vamos usar a função `add_one` (do crate `add_one`) no crate `adder`. Abra o arquivo `adder/src/main.rs` e adicione uma linha `use` no topo para trazer o novo crate de biblioteca `add_one` para o escopo. Em seguida, altere a função `main` para chamar a função `add_one`, como na Listagem 14-7.

Nome do arquivo: `adder/src/main.rs`

```rust
use add_one;

fn main() {
    let num = 10;
    println!(
        "Hello, world! {num} plus one is {}!",
        add_one::add_one(num)
    );
}
```

Listagem 14-7: Usando o crate de biblioteca `add_one` do crate `adder`

Vamos construir o workspace executando `cargo build` no diretório _add_ de nível superior!

```bash
$ cargo build
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68s
```

Para executar o crate binário do diretório `add`, podemos especificar qual pacote no workspace queremos executar usando o argumento `-p` e o nome do pacote com `cargo run`:

```bash
$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/adder`
Hello, world! 10 plus one is 11!
```

Isso executa o código em `adder/src/main.rs`, que depende do crate `add_one`.
