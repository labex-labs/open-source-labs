# Introdução

Neste laboratório, exploraremos a estrutura `Path` em Rust, que representa caminhos de arquivos no sistema de arquivos subjacente. Ela vem em duas versões: `posix::Path` para sistemas tipo UNIX e `windows::Path` para Windows. A estrutura `Path` pode ser criada a partir de um `OsStr` e fornece vários métodos para recuperar informações do arquivo ou diretório apontado pelo caminho. É importante notar que um `Path` é imutável, e sua versão possuída é chamada `PathBuf`, que pode ser modificada no local. A relação entre `Path` e `PathBuf` é semelhante àquela entre `str` e `String`.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
