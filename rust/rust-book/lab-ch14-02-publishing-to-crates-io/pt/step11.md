# Descontinuando Versões do Crates.io com cargo yank

Embora você não possa remover versões anteriores de uma crate, você pode impedir que projetos futuros as adicionem como uma nova dependência. Isso é útil quando uma versão da crate está quebrada por um motivo ou outro. Em tais situações, o Cargo suporta o "yanking" de uma versão da crate.

_Yanking_ uma versão impede que novos projetos dependam dessa versão, permitindo que todos os projetos existentes que dependem dela continuem. Essencialmente, um yank significa que todos os projetos com um _Cargo.lock_ não serão interrompidos, e quaisquer futuros arquivos _Cargo.lock_ gerados não usarão a versão yanked.

Para fazer o yank de uma versão de uma crate, no diretório da crate que você publicou anteriormente, execute `cargo yank` e especifique qual versão você deseja fazer o yank. Por exemplo, se publicamos uma crate chamada `guessing_game` versão 1.0.1 e queremos fazer o yank dela, no diretório do projeto para `guessing_game` executaríamos:

```bash
$ cargo yank --vers 1.0.1
Updating crates.io index
Yank guessing_game@1.0.1
```

Adicionando `--undo` ao comando, você também pode desfazer um yank e permitir que os projetos comecem a depender de uma versão novamente:

```bash
$ cargo yank --vers 1.0.1 --undo
Updating crates.io index
Unyank guessing_game@1.0.1
```

Um yank _não_ exclui nenhum código. Ele não pode, por exemplo, excluir segredos carregados acidentalmente. Se isso acontecer, você deve redefinir esses segredos imediatamente.
