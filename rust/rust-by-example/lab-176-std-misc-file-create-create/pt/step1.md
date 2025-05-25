# `create`

A função `create` abre um ficheiro em modo de escrita exclusiva. Se o ficheiro já existia, o conteúdo antigo é destruído. Caso contrário, um novo ficheiro é criado.

```rust
static LOREM_IPSUM: &str =
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
";

use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("lorem_ipsum.txt");
    let display = path.display();

    // Abre um ficheiro em modo de escrita exclusiva, retorna `io::Result<File>`
    let mut file = match File::create(&path) {
        Err(why) => panic!("não foi possível criar {}: {}", display, why),
        Ok(file) => file,
    };

    // Escreve a string `LOREM_IPSUM` em `file`, retorna `io::Result<()>`
    match file.write_all(LOREM_IPSUM.as_bytes()) {
        Err(why) => panic!("não foi possível escrever em {}: {}", display, why),
        Ok(_) => println!("escrita bem-sucedida em {}", display),
    }
}
```

Eis a saída esperada em caso de sucesso:

```shell
$ rustc create.rs && ./create
escrita bem-sucedida em lorem_ipsum.txt
$ cat lorem_ipsum.txt
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

(Como no exemplo anterior, recomenda-se testar este exemplo em condições de falha.)

A estrutura `OpenOptions` pode ser usada para configurar como um ficheiro é aberto.
