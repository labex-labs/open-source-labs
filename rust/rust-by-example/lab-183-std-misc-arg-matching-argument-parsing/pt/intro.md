# Introdução

Neste laboratório, temos um exemplo de análise de argumentos usando correspondência de padrões em Rust. O programa recebe argumentos da linha de comando e executa diferentes operações com base no número e tipo de argumentos passados. Se nenhum argumento for passado, imprime uma mensagem. Se um único argumento for passado e puder ser analisado como o inteiro 42, imprime "This is the answer!". Se um comando e um argumento inteiro forem passados, executa uma operação de aumento ou diminuição no inteiro. Se qualquer outro número de argumentos for passado, exibe uma mensagem de ajuda explicando o uso correto do programa.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
