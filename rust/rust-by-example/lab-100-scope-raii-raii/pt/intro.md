# Introdução

Neste laboratório, exploraremos o conceito de RAII em Rust, que impõe que a aquisição de recursos seja a inicialização (resource acquisition is initialization). Isso significa que quando os objetos saem do escopo, seus destrutores são chamados e seus recursos próprios são liberados, eliminando a necessidade de gerenciamento manual de memória e garantindo proteção contra vazamentos de recursos (resource leak bugs). Também aprenderemos sobre o trait `Drop` em Rust, que permite que a lógica de destrutor personalizada seja implementada para tipos que a exigem.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
