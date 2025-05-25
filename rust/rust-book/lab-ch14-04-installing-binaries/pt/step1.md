# Instalando Binários com cargo install

O comando `cargo install` permite que você instale e use crates binários localmente. Isso não se destina a substituir pacotes do sistema; é uma maneira conveniente para os desenvolvedores Rust instalarem ferramentas que outros compartilharam em *https://crates.io*. Observe que você só pode instalar pacotes que possuem alvos binários. Um _alvo binário_ é o programa executável que é criado se o crate tiver um arquivo `src/main.rs` ou outro arquivo especificado como binário, em oposição a um alvo de biblioteca que não é executável por si só, mas é adequado para inclusão em outros programas. Normalmente, os crates têm informações no arquivo _README_ sobre se um crate é uma biblioteca, possui um alvo binário ou ambos.

Todos os binários instalados com `cargo install` são armazenados na pasta `bin` da raiz da instalação. Se você instalou o Rust usando `rustup.rs` e não possui nenhuma configuração personalizada, este diretório será \_$HOME/.cargo/bin_. Certifique-se de que esse diretório esteja no seu `$PATH`para poder executar programas que você instalou com`cargo install`.

Por exemplo, no Capítulo 12, mencionamos que existe uma implementação Rust da ferramenta `grep` chamada `ripgrep` para pesquisar arquivos. Para instalar `ripgrep`, podemos executar o seguinte:

```bash
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v13.0.0
  Downloaded 1 crate (243.3 KB) in 0.88s
  Installing ripgrep v13.0.0
   --snip--
   Compiling ripgrep v13.0.0
    Finished release [optimized + debuginfo] target(s) in 3m 10s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v13.0.0` (executable `rg`)
```

A penúltima linha da saída mostra a localização e o nome do binário instalado, que no caso de `ripgrep` é `rg`. Contanto que o diretório de instalação esteja no seu `$PATH`, como mencionado anteriormente, você pode então executar `rg --help` e começar a usar uma ferramenta mais rápida e "Rustier" para pesquisar arquivos!
