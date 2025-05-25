# `open`

A função `open` pode ser usada para abrir um arquivo em modo de leitura somente.

Um objeto `File` possui um recurso, o descritor de arquivo, e cuida do fechamento do arquivo quando é `drop`ado.

```rust
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // Cria um caminho para o arquivo desejado
    let path = Path::new("hello.txt");
    let display = path.display();

    // Abre o caminho em modo de leitura somente, retorna `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("não foi possível abrir {}: {}", display, why),
        Ok(file) => file,
    };

    // Lê o conteúdo do arquivo para uma string, retorna `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("não foi possível ler {}: {}", display, why),
        Ok(_) => print!("{} contém:\n{}", display, s),
    }

    // `file` sai de escopo, e o arquivo "hello.txt" é fechado
}
```

Aqui está a saída esperada em caso de sucesso:

```shell
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt contém:
Hello World!
```

(É recomendado testar o exemplo anterior em diferentes condições de falha: `hello.txt` não existe, ou `hello.txt` não é legível, etc.)
