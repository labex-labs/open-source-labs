# Construindo e Executando um Projeto Cargo

Agora, vamos ver o que é diferente quando construímos e executamos o programa "Hello, world!" com o Cargo! Do seu diretório `hello_cargo`, construa seu projeto digitando o seguinte comando:

```bash
$ cargo build
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs
```

Este comando cria um arquivo executável em `target/debug/hello_cargo` em vez de no seu diretório atual. Como a construção padrão é uma construção de depuração (debug), o Cargo coloca o binário em um diretório chamado `debug`. Você pode executar o executável com este comando:

```bash
$ ./target/debug/hello_cargo
Hello, world!
```

Se tudo correr bem, `Hello, world!` deve ser impresso no terminal. Executar `cargo build` pela primeira vez também faz com que o Cargo crie um novo arquivo no nível superior: _Cargo.lock_. Este arquivo acompanha as versões exatas das dependências em seu projeto. Este projeto não tem dependências, então o arquivo é um pouco esparso. Você nunca precisará alterar este arquivo manualmente; o Cargo gerencia seu conteúdo para você.

Acabamos de construir um projeto com `cargo build` e executamos com `./target/debug/hello_cargo`, mas também podemos usar `cargo run` para compilar o código e, em seguida, executar o executável resultante, tudo em um único comando:

```bash
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Usar `cargo run` é mais conveniente do que ter que se lembrar de executar `cargo build` e, em seguida, usar todo o caminho para o binário, então a maioria dos desenvolvedores usa `cargo run`.

Observe que desta vez não vimos a saída indicando que o Cargo estava compilando `hello_cargo`. O Cargo descobriu que os arquivos não foram alterados, então não reconstruiu, mas apenas executou o binário. Se você tivesse modificado seu código-fonte, o Cargo teria reconstruído o projeto antes de executá-lo, e você teria visto esta saída:

```bash
$ cargo run
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

O Cargo também fornece um comando chamado `cargo check`. Este comando verifica rapidamente seu código para garantir que ele compile, mas não produz um executável:

```bash
$ cargo check
   Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

Por que você não gostaria de um executável? Frequentemente, `cargo check` é muito mais rápido do que `cargo build` porque ele ignora a etapa de produção de um executável. Se você estiver continuamente verificando seu trabalho enquanto escreve o código, usar `cargo check` acelerará o processo de informá-lo se seu projeto ainda está compilando! Como tal, muitos Rustaceans executam `cargo check` periodicamente enquanto escrevem seu programa para garantir que ele compile. Então eles executam `cargo build` quando estão prontos para usar o executável.

Vamos recapitular o que aprendemos até agora sobre o Cargo:

- Podemos criar um projeto usando `cargo new`.
- Podemos construir um projeto usando `cargo build`.
- Podemos construir e executar um projeto em uma etapa usando `cargo run`.
- Podemos construir um projeto sem produzir um binário para verificar erros usando `cargo check`.
- Em vez de salvar o resultado da construção no mesmo diretório que nosso código, o Cargo o armazena no diretório `target/debug`.

Uma vantagem adicional de usar o Cargo é que os comandos são os mesmos, não importa em qual sistema operacional você esteja trabalhando. Portanto, neste ponto, não forneceremos mais instruções específicas para Linux e macOS versus Windows.
