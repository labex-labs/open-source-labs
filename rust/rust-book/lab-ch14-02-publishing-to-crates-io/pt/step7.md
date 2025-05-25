# Configurando uma Conta no Crates.io

Antes de poder publicar qualquer crate, você precisa criar uma conta em *https://crates.io* e obter um token de API. Para fazer isso, visite a página inicial em *https://crates.io* e faça login através de uma conta do GitHub. (A conta do GitHub é atualmente um requisito, mas o site pode suportar outras formas de criar uma conta no futuro.) Depois de fazer login, visite as configurações da sua conta em *https://crates.io/me* e recupere sua chave de API. Em seguida, execute o comando `cargo login` com sua chave de API, assim:

```bash
cargo login abcdefghijklmnopqrstuvwxyz012345
```

Este comando informará ao Cargo sobre seu token de API e o armazenará localmente em _\~/.cargo/credentials_. Observe que este token é um _segredo_: não o compartilhe com mais ninguém. Se você o compartilhar com alguém por qualquer motivo, deverá revogá-lo e gerar um novo token em *https://crates.io*.
