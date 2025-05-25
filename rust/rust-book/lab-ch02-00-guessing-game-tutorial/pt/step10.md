# Usando um Crate para Obter Mais Funcionalidade

Lembre-se que um crate é uma coleção de arquivos de código-fonte Rust. O projeto que estamos construindo é um _crate binário_, que é um executável. O crate `rand` é um _crate de biblioteca_, que contém código que se destina a ser usado em outros programas e não pode ser executado por conta própria.

A coordenação de crates externos pelo Cargo é onde o Cargo realmente se destaca. Antes de podermos escrever código que usa `rand`, precisamos modificar o arquivo `Cargo.toml` para incluir o crate `rand` como uma dependência. Abra esse arquivo agora e adicione a seguinte linha no final, abaixo do cabeçalho da seção `[dependencies]` que o Cargo criou para você. Certifique-se de especificar `rand` exatamente como fizemos aqui, com este número de versão, ou os exemplos de código neste tutorial podem não funcionar:

Nome do arquivo: `Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

No arquivo `Cargo.toml`, tudo o que segue um cabeçalho faz parte dessa seção que continua até que outra seção comece. Em `[dependencies]` você informa ao Cargo quais crates externos seu projeto depende e quais versões desses crates você precisa. Neste caso, especificamos o crate `rand` com o especificador de versão semântica `0.8.5`. O Cargo entende o Semantic Versioning (às vezes chamado de _SemVer_), que é um padrão para escrever números de versão. O especificador `0.8.5` é na verdade uma abreviação de `^0.8.5`, o que significa qualquer versão que seja pelo menos 0.8.5, mas abaixo de 0.9.0.

O Cargo considera que essas versões têm APIs públicas compatíveis com a versão 0.8.5, e essa especificação garante que você obterá o último lançamento de patch que ainda compilará com o código neste capítulo. Qualquer versão 0.9.0 ou superior não tem garantia de ter a mesma API do que os exemplos a seguir usam.

Agora, sem alterar nenhum código, vamos construir o projeto, conforme mostrado na Listagem 2-2.

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

Listagem 2-2: A saída da execução de `cargo build` após adicionar o crate `rand` como uma dependência

Você pode ver números de versão diferentes (mas todos serão compatíveis com o código, graças ao SemVer!) e linhas diferentes (dependendo do sistema operacional), e as linhas podem estar em uma ordem diferente.

Quando incluímos uma dependência externa, o Cargo busca as versões mais recentes de tudo o que essa dependência precisa do _registry_, que é uma cópia dos dados do Crates.io em *https://crates.io*. Crates.io é onde as pessoas no ecossistema Rust postam seus projetos Rust de código aberto para que outros usem.

Após atualizar o registro, o Cargo verifica a seção `[dependencies]` e baixa quaisquer crates listados que ainda não foram baixados. Neste caso, embora tenhamos listado apenas `rand` como uma dependência, o Cargo também pegou outros crates dos quais `rand` depende para funcionar. Após baixar os crates, o Rust os compila e, em seguida, compila o projeto com as dependências disponíveis.

Se você executar imediatamente `cargo build` novamente sem fazer nenhuma alteração, não obterá nenhuma saída além da linha `Finished`. O Cargo sabe que já baixou e compilou as dependências, e você não alterou nada sobre elas no seu arquivo `Cargo.toml`. O Cargo também sabe que você não alterou nada sobre seu código, então ele também não recompila isso. Sem nada para fazer, ele simplesmente sai.

Se você abrir o arquivo `src/main.rs`, fizer uma alteração trivial e, em seguida, salvá-lo e construir novamente, você verá apenas duas linhas de saída:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

Essas linhas mostram que o Cargo só atualiza a compilação com sua pequena alteração no arquivo `src/main.rs`. Suas dependências não foram alteradas, então o Cargo sabe que pode reutilizar o que já baixou e compilou para elas.
