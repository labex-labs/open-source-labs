# Introdução

Neste laboratório, temos algum código Rust que demonstra o uso de _lifetimes_ (tempo de vida) em _structs_ (estruturas). O código inclui uma _struct_ chamada `Borrowed` que contém uma referência a um `i32`, e a referência deve sobreviver à própria _struct_. Há também uma _struct_ chamada `NamedBorrowed` com duas referências a `i32`, ambas as quais devem sobreviver à _struct_. Adicionalmente, existe um _enum_ (enumeração) chamado `Either` que pode ser um `i32` ou uma referência a um, e a referência deve sobreviver ao _enum_. Finalmente, o código cria instâncias dessas _structs_ e _enum_, e imprime seus conteúdos para demonstrar o uso de _lifetimes_ em Rust.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
