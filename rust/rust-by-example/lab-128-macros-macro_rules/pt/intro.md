# Introdução

Neste laboratório, exploraremos o poderoso sistema de macros fornecido pelo Rust, que permite a metaprogramação através da expansão de macros em árvores de sintaxe abstrata (AST - Abstract Syntax Trees). A macro `macro_rules!` é usada para criar macros, e elas se distinguem das funções pelo ponto de exclamação `!`. Macros são úteis para evitar a repetição de código, criar linguagens específicas de domínio e definir interfaces variádicas para funções que podem receber um número variável de argumentos.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
