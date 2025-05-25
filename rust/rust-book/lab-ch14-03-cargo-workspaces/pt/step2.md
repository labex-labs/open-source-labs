# Criando um Workspace (Espaço de Trabalho)

Um _workspace_ (espaço de trabalho) é um conjunto de pacotes que compartilham o mesmo _Cargo.lock_ e diretório de saída. Vamos criar um projeto usando um workspace — usaremos código trivial para que possamos nos concentrar na estrutura do workspace. Existem várias maneiras de estruturar um workspace, então mostraremos apenas uma maneira comum. Teremos um workspace contendo um binário e duas bibliotecas. O binário, que fornecerá a funcionalidade principal, dependerá das duas bibliotecas. Uma biblioteca fornecerá uma função `add_one` e a outra biblioteca uma função `add_two`. Esses três crates farão parte do mesmo workspace. Começaremos criando um novo diretório para o workspace:

```bash
mkdir add
cd add
```

Em seguida, no diretório `add`, criamos o arquivo `Cargo.toml` que configurará todo o workspace. Este arquivo não terá uma seção `[package]`. Em vez disso, ele começará com uma seção `[workspace]` que nos permitirá adicionar membros ao workspace, especificando o caminho para o pacote com nosso crate binário; neste caso, esse caminho é _adder_:

Nome do arquivo: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
]
```

Em seguida, criaremos o crate binário `adder` executando `cargo new` dentro do diretório `add`:

```bash
$ cargo new adder
     Created binary (application) `adder` package
```

Neste ponto, podemos construir o workspace executando `cargo build`. Os arquivos em seu diretório `add` devem ser semelhantes a isto:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

O workspace tem um diretório `target` no nível superior, onde os artefatos compilados serão colocados; o pacote `adder` não tem seu próprio diretório `target`. Mesmo se executássemos `cargo build` de dentro do diretório `adder`, os artefatos compilados ainda acabariam em _add/target_ em vez de `add/adder/target`. O Cargo estrutura o diretório `target` em um workspace assim porque os crates em um workspace devem depender uns dos outros. Se cada crate tivesse seu próprio diretório `target`, cada crate teria que recompilar cada um dos outros crates no workspace para colocar os artefatos em seu próprio diretório `target`. Ao compartilhar um diretório `target`, os crates podem evitar reconstruções desnecessárias.
