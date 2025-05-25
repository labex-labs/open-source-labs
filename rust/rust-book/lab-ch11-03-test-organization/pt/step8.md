# Testes de Integração para Crates Binários

Se nosso projeto for um crate binário que contém apenas um arquivo `src/main.rs` e não tiver um arquivo `src/lib.rs`, não podemos criar testes de integração no diretório `tests` e trazer funções definidas no arquivo `src/main.rs` para o escopo com uma instrução `use`. Apenas os crates de biblioteca expõem funções que outros crates podem usar; crates binários são destinados a serem executados por conta própria.

Esta é uma das razões pelas quais os projetos Rust que fornecem um binário têm um arquivo `src/main.rs` simples que chama a lógica que reside no arquivo `src/lib.rs`. Usando essa estrutura, os testes de integração _podem_ testar o crate de biblioteca com `use` para disponibilizar a funcionalidade importante. Se a funcionalidade importante funcionar, a pequena quantidade de código no arquivo `src/main.rs` também funcionará, e essa pequena quantidade de código não precisa ser testada.
