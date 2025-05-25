# Caminho

A estrutura `Path` representa caminhos de arquivos no sistema de arquivos subjacente. Existem duas variantes de `Path`: `posix::Path`, para sistemas tipo UNIX, e `windows::Path`, para Windows. A pré-definição exporta a variante `Path` específica da plataforma apropriada.

Um `Path` pode ser criado a partir de um `OsStr` e fornece vários métodos para obter informações do arquivo/diretório apontado pelo caminho.

Um `Path` é imutável. A versão possuída de `Path` é `PathBuf`. A relação entre `Path` e `PathBuf` é semelhante à de `str` e `String`: um `PathBuf` pode ser modificado no local e pode ser referenciado para um `Path`.

Observe que um `Path` não é internamente representado como uma string UTF-8, mas sim armazenado como um `OsString`. Portanto, converter um `Path` para um `&str` não é gratuito e pode falhar (um `Option` é retornado). No entanto, um `Path` pode ser livremente convertido para um `OsString` ou `&OsStr` usando `into_os_string` e `as_os_str`, respectivamente.

```rust
use std::path::Path;

fn main() {
    // Cria um `Path` a partir de um `&'static str`
    let path = Path::new(".");

    // O método `display` retorna uma estrutura `Display`ável
    let _display = path.display();

    // `join` mescla um caminho com um contêiner de bytes usando o separador específico do sistema operacional e retorna um `PathBuf`
    let mut new_path = path.join("a").join("b");

    // `push` estende o `PathBuf` com um `&Path`
    new_path.push("c");
    new_path.push("myfile.tar.gz");

    // `set_file_name` atualiza o nome do arquivo do `PathBuf`
    new_path.set_file_name("package.tgz");

    // Converte o `PathBuf` em uma fatia de string
    match new_path.to_str() {
        None => panic!("novo caminho não é uma sequência UTF-8 válida"),
        Some(s) => println!("novo caminho é {}", s),
    }
}
```

Certifique-se de verificar outros métodos `Path` (`posix::Path` ou `windows::Path`) e a estrutura `Metadata`.
