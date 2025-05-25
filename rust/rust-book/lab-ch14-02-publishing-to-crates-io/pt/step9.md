# Publicando no Crates.io

Agora que você criou uma conta, salvou seu token de API, escolheu um nome para sua crate e especificou os metadados necessários, você está pronto para publicar! Publicar uma crate faz o upload de uma versão específica para *https://crates.io* para que outros possam usar.

Tenha cuidado, porque uma publicação é _permanente_. A versão nunca pode ser sobrescrita e o código não pode ser excluído. Um dos principais objetivos do Crates.io é atuar como um arquivo permanente de código para que as compilações de todos os projetos que dependem de crates de *https://crates.io* continuem funcionando. Permitir exclusões de versões tornaria impossível cumprir esse objetivo. No entanto, não há limite para o número de versões de crate que você pode publicar.

Execute o comando `cargo publish` novamente. Ele deve ter sucesso agora:

```bash
$ cargo publish
    Updating crates.io index
   Packaging guessing_game v0.1.0 (file:///projects/guessing_game)
   Verifying guessing_game v0.1.0 (file:///projects/guessing_game)
   Compiling guessing_game v0.1.0
(file:///projects/guessing_game/target/package/guessing_game-0.1.0)
    Finished dev [unoptimized + debuginfo] target(s) in 0.19s
   Uploading guessing_game v0.1.0 (file:///projects/guessing_game)
```

Parabéns! Agora você compartilhou seu código com a comunidade Rust, e qualquer pessoa pode facilmente adicionar sua crate como uma dependência de seu projeto.
