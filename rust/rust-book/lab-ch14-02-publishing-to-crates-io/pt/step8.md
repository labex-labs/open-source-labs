# Adicionando Metadados a uma Nova Crate

Digamos que você tenha uma crate que deseja publicar. Antes de publicar, você precisará adicionar alguns metadados na seção `[package]` do arquivo `Cargo.toml` da crate.

Sua crate precisará de um nome único. Enquanto você estiver trabalhando em uma crate localmente, você pode nomeá-la como quiser. No entanto, os nomes das crates em *https://crates.io* são alocados por ordem de chegada. Uma vez que um nome de crate é usado, ninguém mais pode publicar uma crate com esse nome. Antes de tentar publicar uma crate, pesquise o nome que você deseja usar. Se o nome já foi usado, você precisará encontrar outro nome e editar o campo `name` no arquivo `Cargo.toml` na seção `[package]` para usar o novo nome para publicação, assim:

Nome do arquivo: `Cargo.toml`

```tomlrust
[package]
name = "guessing_game"
```

Mesmo que você tenha escolhido um nome único, ao executar `cargo publish` para publicar a crate neste ponto, você receberá um aviso e, em seguida, um erro:

```bash
$ cargo publish
    Updating crates.io index
warning: manifest has no description, license, license-file, documentation,
homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata
for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields:
description, license. Please see https://doc.rust-
lang.org/cargo/reference/manifest.html for how to upload metadata
```

Isso resulta em um erro porque você está faltando algumas informações cruciais: uma descrição e uma licença são necessárias para que as pessoas saibam o que sua crate faz e sob quais termos elas podem usá-la. Em `Cargo.toml`, adicione uma descrição que seja apenas uma ou duas frases, porque ela aparecerá com sua crate nos resultados da pesquisa. Para o campo `license`, você precisa fornecer um _valor de identificador de licença_. O Software Package Data Exchange (SPDX) da Linux Foundation em *http://spdx.org/licenses* lista os identificadores que você pode usar para este valor. Por exemplo, para especificar que você licenciou sua crate usando a Licença MIT, adicione o identificador `MIT`:

Nome do arquivo: `Cargo.toml`

```toml
[package]
name = "guessing_game"
license = "MIT"
```

Se você deseja usar uma licença que não aparece no SPDX, você precisa colocar o texto dessa licença em um arquivo, incluir o arquivo em seu projeto e, em seguida, usar `license-file` para especificar o nome desse arquivo em vez de usar a chave `license`.

Orientação sobre qual licença é apropriada para seu projeto está além do escopo deste livro. Muitas pessoas na comunidade Rust licenciam seus projetos da mesma forma que o Rust, usando uma licença dupla de `MIT OR Apache-2.0`. Essa prática demonstra que você também pode especificar vários identificadores de licença separados por `OR` para ter várias licenças para seu projeto.

Com um nome único, a versão, sua descrição e uma licença adicionadas, o arquivo `Cargo.toml` para um projeto que está pronto para ser publicado pode se parecer com isto:

Nome do arquivo: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"
description = "A fun game where you guess what number the
computer has chosen."
license = "MIT OR Apache-2.0"

[dependencies]
```

A documentação do Cargo em *https://doc.rust-lang.org/cargo* descreve outros metadados que você pode especificar para garantir que outros possam descobrir e usar sua crate com mais facilidade.
