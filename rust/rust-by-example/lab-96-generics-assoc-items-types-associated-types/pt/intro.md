# Introdução

Neste laboratório, exploramos o conceito de tipos associados em Rust, que permite melhorar a legibilidade do código definindo tipos internos localmente dentro de um tratado como tipos de saída. Isto é alcançado usando a palavra-chave `type` dentro da definição do tratado. Com tipos associados, as funções que utilizam o tratado não precisam mais expressar explicitamente os tipos `A` e `B`, tornando o código mais conciso e flexível. Reescrevemos um exemplo de uma seção anterior usando tipos associados para ilustrar seu uso na prática.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
