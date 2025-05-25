# Introdução

Neste laboratório, temos um fragmento de código em Rust que demonstra como criar threads nativas do sistema operacional usando a função `spawn` e um fecho (closure) móvel. O código cria um vetor para armazenar as threads criadas, itera através de um intervalo de números para criar várias threads e imprime uma mensagem identificando o número de cada thread. Finalmente, a thread principal aguarda o término de cada thread criada usando a função `join`.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
