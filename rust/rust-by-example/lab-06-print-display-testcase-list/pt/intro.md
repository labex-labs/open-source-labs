# Introdução

Neste laboratório, estamos implementando `fmt::Display` para uma estrutura chamada `List` que contém um `Vec` em Rust. O desafio é lidar com cada elemento sequencialmente usando a macro `write!`, pois ela gera um `fmt::Result` que precisa ser tratado adequadamente. Para resolver isso, podemos usar o operador `?` para verificar se `write!` retorna um erro e retorná-lo, caso retorne, caso contrário, continuar com a execução. Ao implementar `fmt::Display` para `List`, podemos iterar sobre os elementos no vetor e imprimi-los entre colchetes, separados por vírgulas. A tarefa é modificar o programa para também imprimir o índice de cada elemento no vetor. A saída esperada após a modificação é `[0: 1, 1: 2, 2: 3]`.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
