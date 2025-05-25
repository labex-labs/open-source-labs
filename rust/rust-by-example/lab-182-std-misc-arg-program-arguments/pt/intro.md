# Introdução

Neste laboratório, você pode acessar argumentos de linha de comando em Rust usando a função `std::env::args`, que retorna um iterador que gera uma `String` para cada argumento. O primeiro argumento no vetor retornado é o caminho usado para chamar o programa, enquanto o restante dos argumentos são os parâmetros da linha de comando. Alternativamente, você pode usar bibliotecas como `clap` para um gerenciamento mais avançado de argumentos de linha de comando.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
