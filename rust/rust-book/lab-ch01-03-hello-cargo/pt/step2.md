# Criando um Projeto com Cargo

Vamos criar um novo projeto usando o Cargo e ver como ele difere do nosso projeto original "Hello, world!". Navegue de volta para o seu diretório `project` (ou onde quer que você tenha decidido armazenar seu código). Em seguida, em qualquer sistema operacional, execute o seguinte:

```bash
cd ~/project
cargo new hello_cargo
cd hello_cargo
```

O primeiro comando cria um novo diretório e projeto chamado _hello_cargo_. Nomeamos nosso projeto _hello_cargo_, e o Cargo cria seus arquivos em um diretório com o mesmo nome.

Entre no diretório `hello_cargo` e liste os arquivos. Você verá que o Cargo gerou dois arquivos e um diretório para nós: um arquivo `Cargo.toml` e um diretório `src` com um arquivo `main.rs` dentro.

Ele também inicializou um novo repositório Git junto com um arquivo _.gitignore_. Os arquivos Git não serão gerados se você executar `cargo new` dentro de um repositório Git existente; você pode substituir esse comportamento usando `cargo new --vcs=git`.

> Nota: Git é um sistema de controle de versão comum. Você pode alterar `cargo new` para usar um sistema de controle de versão diferente ou nenhum sistema de controle de versão usando a flag `--vcs`. Execute `cargo new --help` para ver as opções disponíveis.

Abra `Cargo.toml` no seu editor de texto de sua escolha. Ele deve ser semelhante ao código na Listagem 1-2.

Nome do arquivo: `Cargo.toml`

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]
```

Listagem 1-2: Conteúdo de `Cargo.toml` gerado por `cargo new`

Este arquivo está no formato _TOML_ (_Tom's Obvious, Minimal Language_), que é o formato de configuração do Cargo.

A primeira linha, `[package]`, é um cabeçalho de seção que indica que as instruções a seguir estão configurando um pacote. À medida que adicionamos mais informações a este arquivo, adicionaremos outras seções.

As três linhas seguintes definem as informações de configuração que o Cargo precisa para compilar seu programa: o nome, a versão e a edição do Rust a serem usados. Falaremos sobre a chave `edition` no Apêndice E.

A última linha, `[dependencies]`, é o início de uma seção para você listar quaisquer dependências do seu projeto. Em Rust, pacotes de código são referidos como _crates_. Não precisaremos de nenhum outro crate para este projeto, mas precisaremos no primeiro projeto no Capítulo 2, então usaremos esta seção de dependências então.

Agora abra `src/main.rs` e dê uma olhada:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

O Cargo gerou um programa "Hello, world!" para você, assim como o que escrevemos na Listagem 1-1! Até agora, as diferenças entre nosso projeto e o projeto que o Cargo gerou são que o Cargo colocou o código no diretório `src` e temos um arquivo de configuração `Cargo.toml` no diretório superior.

O Cargo espera que seus arquivos de origem residam dentro do diretório `src`. O diretório do projeto de nível superior é apenas para arquivos README, informações de licença, arquivos de configuração e qualquer outra coisa não relacionada ao seu código. Usar o Cargo ajuda você a organizar seus projetos. Há um lugar para tudo, e tudo está em seu lugar.

Se você iniciou um projeto que não usa o Cargo, como fizemos com o projeto "Hello, world!", você pode convertê-lo em um projeto que usa o Cargo. Mova o código do projeto para o diretório `src` e crie um arquivo `Cargo.toml` apropriado.
