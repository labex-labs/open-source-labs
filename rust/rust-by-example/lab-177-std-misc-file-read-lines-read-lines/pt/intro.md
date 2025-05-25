# Introdução

Neste laboratório, temos uma implementação ingênua e uma implementação mais eficiente para ler linhas de um arquivo em Rust. A abordagem ingênua utiliza `read_to_string` para ler o arquivo em uma única string e, em seguida, dividi-la em linhas, enquanto a abordagem mais eficiente utiliza um `BufReader` para ler o arquivo linha por linha sem carregar todo o conteúdo na memória.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
